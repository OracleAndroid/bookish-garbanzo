import pynput 
from pynput import keyboard
from pynput.keyboard import Key, Listener  
import logging

#Key stroke listening code. 
COMBINATION = {keyboard.Key.ctrl_l, keyboard.KeyCode(char = 'b')}
current = set()


def on_press(key):        
    logging.info(str(key))
    print('{0} key pressed'.format(key))
    if key in COMBINATION:
        current.add(key)
        if all(k in current for k in COMBINATION):
                print("That's a bingo!")
    if key == keyboard.Key.esc:
        print ('Closing Listener') 
        listener.stop()

def on_release(key):
    logging.info(str(key))
    print('{0} key released'.format(key))


with Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()
