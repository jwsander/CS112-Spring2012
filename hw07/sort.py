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

N = len(nums)
for x in range(N):
    iPos = x
    for i in range(x, N):
        if nums[i] < nums[iPos]:
            iPos = i
    nums[x],nums[iPos] = nums[iPos], nums[x]

print "After sort:"
print nums
