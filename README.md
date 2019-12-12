# manual-revision-of-transcripts
This repo contains our recommendations and tools for manual revision of speech transcripts.

- ``on-linux-in-vim`` suggests how to do it on Linux with the text editor VIM
- ``youtube-subtitle-editor`` suggests how to do it with youtube web editor
- Amara subtitle editor (please add a subdir and a README how to do it)
- Filmtit + Matus Namesny's project (talk to Ondrej Bojar if we could revive this)
- TranscriberAG (http://transag.sourceforge.net/)

## Minimal Annotation Guidelines

Depending on the particular editing environment, please try to adhere to the following annotation rules as much as possible:

- full correct letter casing + punctuation
- one line per sentence
- handling of numbers and abbreviations is unclear; the following options seem equally good, but try to be consistent:
  - spelled out (write down these words to the transcript): ``forty four``, ``Czech Tech`` (if the abbreviation was not spelled letter by letter ["C-T-U"])
  - condensed (write down abbreviations to transcripts): ``44``, ``CTU``
  - In any case avoid _expanding_ what was said, so do not write ``Czech Technical University`` when the person said CzechTech
- in most cases transcribe exactly what was said. this includes: 
	* repeated words
  * grammatical errors
  * semantic errors, e.g. incorrect word choice in non-native speech
  * exceptions from this include transcribing with presentation in mind, e.g. youtube subitles, where we should aim for readability
