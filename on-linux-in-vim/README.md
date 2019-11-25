# Revising ASR Transcript in VIM on Linux

Recommended usage:

```
# symlink your favourite vimrc to .vimrc (in this directory)
ln -s ondrej-vimrc .vimrc
```

## Ondrej's Solution

Run ``mplayer`` in slave mode:

```
mkfifo /tmp/mplayer-slave-fifo-file
mplayer -slave -input file=/tmp/mplayer-slave-fifo-file YOUR-INPUT-SOUND-FILE
```

Launch ``vim`` with Ondrej's vimrc:
```
ln -s ondrej-vimrc .vimrc
vim YOUR-INITIAL-TRANSCRIPT-FILE
```

See ``ondrej-vimrc`` for key bindings.

## Jonas' Solution

Play audio by sox command `play` for example:
```
play file.wav
```
Now in separate tab of terminal open vim with the transcript you want to correct.
I use shortcuts ctrl+p to stop the audio and ctrl+l to play it again (you can change the mapping in vimrc).
I have remapped my escape key to jump to normal mode to more convenient combination of `jj` which is right in the middle of a keyboard. I think that it is more efficient to remap it to that as especially during transcript correction you jump between vim modes quite often so it is nice to save the effort of stretching all the way to `esc` button. 
Inside vim I use the standard shortcuts for modifying the text:
```
ciw/diw - to change whole word when inside it and go to insert mode/normal mode
ce/de   - change from here to the end of word and go to insert mode/normal mode
/       - for searching specific word
e/b     - moving foorward/backwards between words
```
I find it also convenient to follow the audio with a cursor and to have highlited row on which I currently find myself by puttion `set cursorline` to `.vimrc`. 


