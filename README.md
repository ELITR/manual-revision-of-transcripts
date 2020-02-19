# manual-revision-of-transcripts
This repo contains our recommendations and tools for manual revision of speech transcripts.

- ``on-linux-in-vim`` suggests how to do it on Linux with the text editor VIM
- ``youtube-subtitle-editor`` suggests how to do it with youtube web editor
- ``TLP``, the TransLectures Platform from UPV could be a great option for us.
- Amara (https://amara.org/) subtitle editor (please add a subdir and a README how to do it)
- Filmtit + Matus Namesny's project (talk to Ondrej Bojar if we could revive this)
- **TranscriberAG** (http://transag.sourceforge.net/) seems buggy at first but successfully worked for Daniel
- Subtitle Edit (https://www.nikse.dk/subtitleedit) is free, Windows-based
  - We could emit our ASR as subtitles and use Subtitle Edit to correct the transcript.
- if you want to transcribe publicly available sources (e.g. youtube videos) you can use oTranscribe (https://otranscribe.com/)

## Minimal Annotation Guidelines

Depending on the particular editing environment, please try to adhere to the following annotation rules as much as possible:

- Full correct letter casing + punctuation
- One line per sentence
  + When in doubt if there was or was not a sentence boundary, *please mark it as if it was there*. We prefer more shorter sentences.
- Handling of numbers and abbreviations is unclear; the following options seem equally good, but try to be consistent:
  - spelled out (write down these words to the transcript): ``forty four``, ``Czech Tech`` (if the abbreviation was not spelled letter by letter ["C-T-U"])
  - condensed (write down abbreviations to transcripts): ``44``, ``CTU``
  - In any case avoid _expanding_ what was said, so do not write ``Czech Technical University`` when the person said CzechTech
- In most cases transcribe exactly the words that were said. This includes: 
  * Repeated words
  * Grammatical errors
  * Semantic errors, e.g. incorrect word choice in non-native speech
  * Exceptions from this include transcribing sound where the transcript is supposed to be publicly released. For instance when transcribing youtube videos and we directly want to keep the subtitles public, we should aim a little more for readability over verity.
