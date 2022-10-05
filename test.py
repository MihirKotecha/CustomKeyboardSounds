from time import time
from pynput.keyboard import Listener
from pynput import keyboard
from playsound import playsound
import time
def on_press(key):
    print(key)
    playsound(r"C:\Users\Mihir Kotecha\Desktop\Key Logger\Sound Effects\mk.mp3")
    if(str(key) == 'Key.esc'):
        print("ending Keylogger")
        exit()

with Listener(on_press=on_press) as l:
    l.join()

    


    

