#!/usr/bin/env python
"""
prissybot.py

CS112 Homework 3:   PrissyBot

Prissy bot, the rude chat bot, is just mean!  It does not listen, asks obnoxious questions, and says anything it likes.
"""

n=raw_input("Enter your name:")
print "PrissyBot: Hello there,",n
print n,":",
#makes Name: pop up, like a chat
m=raw_input()
print "PrissyBot: You mean,",m,"sir! I AM your superior, you know. I can prove it, too."
#I COULD have made "PrissyBot:" a variable as well, early on. Since I was already halfway through, I didn't have the hear to change it

print "PrissyBot: How about a riddle?"
print "PrissyBot: How do you keep a blockhead waiting?"
print n,":",
l=raw_input()
print "PrissyBot: Nope, not",l,". I'll tell you tomorrow."
#messing with the riddles

print "PrissyBot: Now that you're properly belittled, how about some math?"
print "PrissyBot: Give me a number, any number."
print n,":",
j=int(raw_input())
print "PrissyBot: Can you even count? Come on! Something bigger!"
print n,":",
k=int(raw_input())
#Straightforward data input

print "PrissyBot: Here we go..."
print "PrissyBot: ",j,"minus",k,"is",j-k
print "PrissyBot: ",j,"divided by",k,"is",j/k
print "PrissyBot: ",j,"plus",k,"is",j+k
print "PrissyBot: And",j,"times",k,"is",j*k,",which is coincidentally how many times smarter than you I am."
print "PrissyBot: Trust me, I'm a computer."

print ""
print "PrissyBot: Alright",n,"I'll help you out a bit. You look like you need it."
print "PrissyBot: I can tell the future, you know. Mathemagically."
print "PrissyBot: In what year were you born?"
print n,":",
o=int(raw_input())
#The int() made it work. remember that
print "PrissyBot: Oh, so you are about",2011-o,"years old. Not bad."
#Simple math, numbers and variables
print "PrissyBot: And the day of month you were born on is...?"
print n,":",
p=int(raw_input())
print "PrissyBot: Hmmmmm...According to my calculations, you have about",o/p,"days left to live. Better get off the computer, huh?"
print "PrissyBot: Well, nice knowing you...sort of."
print "PrissyBot: Goodnight!"

