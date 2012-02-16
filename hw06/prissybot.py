#!/usr/bin/env python
"""
prissybot.py

CS112 Homework 3:   PrissyBot

Prissy bot, the rude chat bot, is just mean!  It does not listen, asks obnoxious questions, and says anything it likes.
"""

##Saying Hello
name = raw_input("Enter your name:")
print "PrissyBot: Hello there,",name
print name + ":",
m = raw_input()
print "PrissyBot: You mean, " + "'" + m , "sir!" + "'" + "I AM your superior, you know. I can prove it, too."

##A Riddle
print "PrissyBot: How about a riddle?"
print "PrissyBot: How do you keep a blockhead waiting?"
print name + ":",
guess = raw_input()
print "PrissyBot: Nope, not " + "'" + guess + ".'" + " I'll tell you tomorrow."

##Getting numbers
print "PrissyBot: Now that you're properly belittled, how about some math?"
print "PrissyBot: Give me a number, any number."
print name + ":",
num1 = int(raw_input())
print "PrissyBot: Can you even count? Come on! Something bigger!"
print name + ":",
num2 = int(raw_input())

##Math
print "PrissyBot: Here we go..."
print "PrissyBot: ", num1, "minus", num2, "is", (num1 - num2)
print "PrissyBot: ", num1, "divided by", num2,"is", (num1/num2)
print "PrissyBot: ", num1, "plus", num2, "is", (num1 + num2)
print "PrissyBot: And", num1, "times", num2, "is", (num1*num2), ",which is coincidentally how many times smarter than you I am."
print "PrissyBot: Trust me, I'm a computer."

##Prediction of Future
#Intro
print "" # empty space
print "PrissyBot: Alright " + name + ", I'll help you out a bit. You look like you need it."
print "PrissyBot: I can tell the future, you know. Mathemagically."

#Age Calculation
print "PrissyBot: In what year were you born?"
print name + ":",
yr = int(raw_input())
print "PrissyBot: Oh, so you are about",(2011-yr),"years old. Not bad."

#Death Date
print "PrissyBot: And the day of month you were born on is...?"
print name + ":",
day = int(raw_input())
print "PrissyBot: Hmmmmm...According to my calculations, you have about", (yr/day), "days left to live. Better get off the computer, huh?"
print "PrissyBot: Well, nice knowing you...sort of."
print "PrissyBot: Goodnight!"
