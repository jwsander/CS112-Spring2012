#!/usr/bin/env python

from random import randint

s=1
listLength=int(raw_input("Number of random numbers:"))
list1=[]

##Prints (listLength) amount of random numbers
for _ in range(listLength):
    list1.append(randint(0,20))
print list1

##Sorts them
while s == 1:
    s=0
    for var in range(1,listLength):
        if list1[var-1] > list1[var]:
            t1=list1[s-1]
            t2=list1[s]
            list1[s-1]=t2
            list1[s]=t1
            s=1

print list1
