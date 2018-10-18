#!/usr/bin/env python3

#import regular expression (every script)
import re

#Find and print position
with open('Python_07_nobody.txt','r') as nobody:
 for line in nobody:
  found=re.search(r'Nobody' ,line)
  if found:
   print(found.start())

with open ('Python_07_nobody.txt' , 'r') as nobody, open('writing_nobody.txt' , 'w') as fo:
 for line in nobody:
  michael=re.sub(r'Nobody' , 'Michael' , line)
  print(line)
  print(michael)
  fo.write(michael)



