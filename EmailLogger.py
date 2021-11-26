#!/usr/bin/env python3

import re
fileToRead = 'keylog.txt'
fileToWrite = 'extractedemails.txt'
delimiterInFile = [',', ';']
def validateEmail(strEmail):
    # .* Zero or more characters of any type. 
    if re.match("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                    "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                    "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)", strEmail):
        return True
    return False
def writeFile(listData):
    file = open(fileToWrite, 'w+')
    strData = ""
    for item in listData:
        strData = strData+item+'\n'
    file.write(strData)
listEmail = []
file = open(fileToRead, 'r') 
listLine = file.readlines()
for itemLine in listLine:
    item =str(itemLine)
    for delimeter in delimiterInFile:
        item = item.replace(str(delimeter),' ')
    
    wordList = item.split()
    for word in wordList:
        if(validateEmail(word)):
            listEmail.append(word)
if listEmail:
    uniqEmail = set(listEmail)
    print(len(uniqEmail),"emails collected!")
    writeFile(uniqEmail)
else:
    print("No email found.")
