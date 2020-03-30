#===========================================================
#  Title:  eaftojson
#  Author: Ebrahim Ansari, Ondrej Bojar, Mohammad Mahmoudi
#  Date:   28 March 2020
#  This Project is a part of the framework which is written 
# to evaluate simoltanius translation systems.
#  https://github.com/ELITR/
#===========================================================


#-------------------modules
import os 
import xml.etree.ElementTree as ET
import json 
import subprocess
import argparse
import re
import string

def get_duration(sound_path):
    
    """
    
    Calculate sound time length.
    
    """
    path_of_wav_file = sound_path
    process = subprocess.Popen(['ffmpeg',  '-i', path_of_wav_file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = process.communicate()
    stdout = str(stdout)
    matches = re.search(r"Duration:\s{1}(?P<hours>\d+?):(?P<minutes>\d+?):(?P<seconds>\d+\.\d+?),", str(stdout), re.DOTALL).groupdict()


    duration = (float(matches['hours']) * 360) + (float(matches['minutes']) * 60) + float(matches['seconds'])
    return duration


def text_preprocessing(text):
    """
    
    preprocessing output text
    
    """
    
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    text = re.sub(' +', ' ', text)
    return text

def create_json(time, text, file_path):
    """
     
    Created json file as  json demo. 
     
    """
    audio_filepath = file_path 
    duration = float("%.2f" % time)

    text = text_preprocessing(text)
    temp = dict()
     
    temp['audio_filepath'] = audio_filepath
    temp['duration'] = float(duration)
    temp['text'] = text
    return temp



parser = argparse.ArgumentParser(description="this script eaf file and sound and do segmentation.")
parser.add_argument("--sound", help="path of the wave file", type=str)
parser.add_argument("--eaf", help="path of the eaf file", type=str)
parser.add_argument("--out_dir", help="path of the output directories", type=str, default = './outputs/')

args = parser.parse_args()

#--------------------check out directory
if os.path.isdir(args.out_dir):  
    pass
else:
    cmd = 'mkdir -p ' + args.out_dir 
    os.system(cmd)

if args.sound == None:
    print('please insert sound file path')
    sys.exit(1)
if args.eaf == None:
    print('please insert eaf file path')
    sys.exit(1)



# parse an xml file by name
tree = ET.parse(args.eaf)
root = tree.getroot()
TIER = root.find('TIER')
TIME_ORDER = root.find('TIME_ORDER')
#-----------read TIME_SLOT sections
times_order = dict()
time_slots = TIME_ORDER.findall('TIME_SLOT')

for i in time_slots:
    slot_id = i.attrib['TIME_SLOT_ID']
    slot_value = i.attrib['TIME_VALUE']
    times_order[slot_id] = slot_value

#-----------read ALIGNABLE_ANNOTATION
segments = list()
anotations = TIER.findall('ANNOTATION')

for i in anotations:
    anotation = i.find('ALIGNABLE_ANNOTATION')
    start = anotation.attrib['TIME_SLOT_REF1']
    end = anotation.attrib['TIME_SLOT_REF2']
    start = (float(times_order[start]))/1000 
    end = (float(times_order[end]))/1000 
    anotation_value = anotation.find('ANNOTATION_VALUE')
    text = anotation_value.text
    segments.append([text, start, end])

wave_name = args.sound.split('/')
wave_name = wave_name[-1].split('.')
wave_name = '.'.join(wave_name[:-1])

count = 0

for i in segments:
    count_text = "{0:0=3d}".format(count)
    #------------ make a segment wave file
    wave_path = args.out_dir + wave_name + count_text + '.wav'
    t1 = i[1]
    t2 = i[2]
    cmd = "ffmpeg -hide_banner -loglevel panic -i " + str(args.sound) + " -ss " + str(t1) + " -to " + str(t2) + " -c copy  " + wave_path
   
    os.system(cmd)
    print(wave_path, " is created")
    ost_path = args.out_dir + wave_name + count_text + '.OSt'
    #------------- make OSt file
    ost_file = open(ost_path, 'w')
    ost_file.write(i[0])
    ost_file.close()
    print(ost_path, " is created")
    ost_path = os.getcwd() + '/' + ost_path
    text = i[0]
    time = float(t2) - float(t1)

    json_dict = create_json(time, text, wave_path)
    
    json_name = ost_path.split('.')
    json_name = '.'.join(json_name[:-1])
    json_name += '.json' 
    with open(json_name, 'a') as fp: 
        json.dump(json_dict,fp)
        

    print(json_name, " is created")
    count += 1

    
