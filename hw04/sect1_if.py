#!/usr/bin/env python
from hwtools import *

print "Section 1:  If Statements"
print "-----------------------------"

# 1.  Is n even or odd and 2. If so double it.
n = raw_input("Enter a number: ")
n = int(n)

if n/2 == n/2.0:
    print "1. Even"
    print "1. Not odd, so won't multiply because I'm cool that way."
else:
    print "1. Odd"
    print "2.",n*2


# 3. If n is evenly divisible by 3, add four
if n/3 == n/3.0:
    print "3.", n+4
else:
    print "3. Not evenly divisible by 3."


# 4. Grade's letter values (eg. 90-100)
grade=-555
while grade ==-555:
    grade = raw_input("Enter a grade [0-100]: ")
    grade = int(grade)
#For trolls
    if grade >100:
        print "Over 100!? IMPOSSIBRU!!!!"
        grade = -555
    elif grade<0:
        print "Negative grade!? IMPOSSIBRU!!!"
        grade = -555
#Grades
if grade ==100:
    print "4. A+, you over-acheiver!"
elif grade >=90 and grade <100:
    print "4. A"
elif grade >=80 and grade <90:
    print "4. B"
elif grade >=70 and grade <80:
    print "4. C"
elif grade >=60 and grade <70:
    print "4. D"
elif grade >0 and grade <50:
    print "4. F"

