follow = 20 #CHANGE HERE HOW MANY PEOPLE YOU WILL FOLLOW
# suggest: do not follow more than 1000 people at once
import pyautogui
import time
import pyperclip
import random

pyautogui.PAUSE = 1 #Set up a 1 second pause after each PyAutoGUI call
find = "find.png" #image to search on screen (needs to be on the same directory as the main.py) 

def main():
    pyautogui.hotkey('alt', 'tab', interval=0.1) #alt+tab to switch to instagram screen
    time.sleep(random.randrange(6,15)/10) #sleep random time

    for n in range (0,follow):
        try:
            found = pyautogui.locateOnScreen(find) #search for: image="find" on the screen
            pyautogui.click(found[0] + 10, found[1] +5, 1, 0.2) #click on image found
            time.sleep(random.randrange(6,15)/10) #sleep random time

        except IOError: #if image="find" is not found (needs to be on the same directory as the main.py)
            print('Image not found')
            break

        except: #if image="find" is not found on screen
            pyautogui.scroll(-5) #scroll screen
            pass
            
    pyautogui.hotkey('alt', 'tab', interval=0.1) #alt+tab to switch to main.py screen
    print("%d people were followed" % (n+1)) #how many people were followed

main()