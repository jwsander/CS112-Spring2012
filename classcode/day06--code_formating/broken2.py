#!/usr/bin/env python

from random import randint

s=1
t=int(raw_input("Number of random numbers:"))
list1=[]

for _ in range(t):
    list1.append(randint(0,20))

print list1

while s:
    s=0
    for var in range(1,t):
        if list1[var-1] > list1[var]:
            t1=list1[i-1]
            t2=list1[i]
            list1[i-1]=t2
            list1[i]=t1
            s=1

print list1
