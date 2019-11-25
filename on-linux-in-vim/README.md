# Revising ASR Transcript in VIM on Linux (Jonas solution)

I like to use vim + keyboard shortcuts. For play and stop of audio I use combination of alt+shift+backspace and for rewinding I use left arrow (I have arrows disabled inside vim so that is does not confuse with inside vim movement).
I have remapped my escape key to jump to normal mode to more convenient combination of `jj` which is right in the middle of a keyboard. I think that it is more efficient to remap it to that as especially during transcript correction you jump between vim modes quite often so it is nice to save the effort of stretching all the way to `esc` button. 
Inside vim I use the standard shortcuts for modifying the text:
```
ciw/diw - to change whole word when inside it and go to insert mode/normal mode
ce/de   - change from here to the end of word and go to insert mode/normal mode
/       - for searching specific word
e/b     - moving foorward/backwards between words
```
I find it also convenient to follow the audio with a cursor and to have highlited row on which I currently find myself by puttion `set cursorline` to `.vimrc`. 


