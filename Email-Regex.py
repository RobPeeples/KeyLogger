#!/usr/bin/env python3

import sys
import re

def emailregex(file):
        with open('keylog.txt', 'r') as file:
                lines=file.readlines()
                lines=[line.rstrip() for line in lines]
                match = re.findall(r'[\w\.-]+@[\w\.-]', lines)
                for i in match:
                        print(i)

def main():
    # Get the filename from the first command line argument
        filename = sys.argv[1]
        if __name__ == '__main__':
                main()
