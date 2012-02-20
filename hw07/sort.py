#!/usr/bin/env python
"""
Selection sort

This is my selection sort, it's not working right!!!
I used this:
    http://en.wikipedia.org/wiki/Selection_sort
"""
from hwtools import input_nums

nums = input_nums()

print "Before sort:"
print nums

length = len(nums)
for x in range(length):
    iPos = x
    for num2 in range(x, length):
        if nums[num2] < nums[iPos]:
            iPos = num2
    nums[x],nums[iPos] = nums[iPos], nums[x]

print "After sort:"
print nums
