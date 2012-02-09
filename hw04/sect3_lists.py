#!/usr/bin/env python
from hwtools import *

print "Section 3:  Lists"
print "-----------------------------"

nums = input_nums()
amount = len(nums)

print "1.", amount, "numbers entered."

# 2.  Append 3 and 5 to nums
nums.append(3)
nums.append(5)
print "2.", nums

# 3.  Remove the last element from nums
print "3.", nums[0:amount+1]


# 4.  Set the 3rd element to 7
nums2=nums[:]
nums2[2]=7
print "4.", nums2





# 5. [ADVANCED] Grab a new list of numbers and add it to the existing one

# print "5.", nums


# 6. [ADVANCED] Make a copy of this new giant list and delete the 2nd 
#    through 4th values

# nums_copy = __
# print "6.", nums, nums_copy

# 7-9. [ADVANCED] Print the following:

# print "7.", nums[__]    # first 3 elements
# print "8.", nums[__]    # last element
# print "9.", nums[__]    # a list of the second element
