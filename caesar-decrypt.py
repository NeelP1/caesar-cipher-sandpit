#!/usr/bin/env python

import sys

word = sys.argv[1]
newWord = ''

for char in word:
    x = 26 + (ord(char) - 3 % 97) if (ord(char) - 3 % 97) < 3 else (ord(char) - 3)
    newWord += chr(x)

print newWord
