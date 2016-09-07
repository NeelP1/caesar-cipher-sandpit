#!/usr/bin/env python
'''Caeser Cipher Encrypter'''

import sys

word = sys.argv[1]
newWord = ''

for char in word:
    #newWord += chr(ord(char) + 3)
    #print chr(ord(char) % 122)
    x = (ord(char) + 3) % 123 if (ord(char) + 3) % 123 >= 97 else (ord(char) + 100) % 123
    newWord += chr(x)

print newWord
