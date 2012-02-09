#!/usr/bin/env python
from hwtools import *

print "Section 4:  For Loops"
print "-----------------------------"

nums = input_nums()
# 1. What is the sum of all the numbers in nums?
total=sum(nums)
print "1.", total


# 2. Print every even number in nums
even = []
for num in nums:
    if num/2==num/2.0:
        even.append(num)
print "2. Even numbers:",even


# 3. Does nums only contain even numbers? 
only_even = False
if len(nums)==len(even):
       only_even = True
else:
        only_even = False

print "3.",
if only_even:
    print "Only even"
else:
    print "Some odd"


# 4. Generate a list every odd number less than 100. Hint: use range()
odds = [range(1,100,2)]
print "4.",odds

# 5. [ADVANCED]  Multiply each element in nums by its index
multiples = []
for num in nums:
    multiples.append(num*nums.index(num))
print "5. Multiples of index:",multiples

