from visual import *
prose = label() # initially blank text
while True: 
    if scene.kb.keys: # event waiting to be processed?
        s = scene.kb.getkey() # get keyboard info
        if len(s) == 1: 
            prose.text += s # append new character
        elif ((s == 'backspace' or s == 'delete') and
                len(prose.text)) > 0: 
            prose.text = prose.text[:-1] # erase letter
        elif s == 'shift+delete': 
            prose.text = '' # erase all text