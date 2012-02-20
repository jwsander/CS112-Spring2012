#!/usr/bin/env python
"""
Binary Search

This was supposed to be a binary search algorithm but it isn't working...
I used the Iterative implementation from here:
    http://en.wikipedia.org/wiki/Binary_search_algorithm
"""
from hwtools import input_nums

nums = input_nums()
nums = sorted(nums)
print "I have sorted your numbers"

x = int(raw_input("Which number should I find: "))
min = 0
max = len(nums)-1

while max >= min:
    mid = (max + min)/ 2
    if nums[mid] == x:
        break
    elif x > nums[mid]:
        min = (mid + 1)
    else:
        max = (mid - 1)

if nums[mid] == x:
    print "Found", x, "at", mid
else:
    print "Could not find", x
