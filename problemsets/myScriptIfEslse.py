#!/usr/bin/env python3

# assign a value to a variable

import sys
my_number = int (sys.argv[1])

if my_number < 0:
  message = "is True"
else:
  message = "is Not True"

print (message)

