#!/usr/bin/env python
from hwtools import *

print "Section 2:  Loops"
print "-----------------------------"

# 1. Keep getting a number from the input (num) until it is a multiple of 3.
num = 1
while num/3 != num/3.0:
    num=raw_input("Enter a magic number:")
    num=int(num)    
print "1.", num

# 2. Counting down by threes
print "2. Countdown from",num
while num>=0:
    print num
    num-=3

# 3. [ADVANCED] Variable countdown 

num2 = int(raw_input("3. Countdown from: "))

# Multiple of three
if num2/3 == num2/3.0:
    while num2>=0:
        print num2
        num2-=3

# Multiple of 2
elif num2/2 == num2/2.0:
    while num2>=0:
        print num2
        num2-=2

# Anything else
else:
    while num2>=0:
        print num2
        num2-=1

