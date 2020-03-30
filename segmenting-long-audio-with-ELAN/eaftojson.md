
# EAF to JSON
Eaftojson is a script to convert eaf (outputs of the ELAN software) and convert it to several segments and then building json file for each segment.
The input is an audio file and a eaf file, and the output is an audio file, a ost file, and a json file for each segment.

#### Requirements 
	
* python3

#### Running 
	
* python eaftojson.py --sound "belgian.OS.wav" --eaf "test.eaf" --out_dir "./outputs/"

#### Parameters
	
* **--sound**: The path of wav file.
* **--eaf**: The path of eaf file. 
* **--out_dir**: the path of output folder (default is "./outputs/") 
