#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles. The last one to grab a stone loses. Features name input and pile size/maximum stones settings.


"""

##Initialization
print "__________________________________________"
print "             Welcome to Nims!             "
print "__________________________________________"

#Name input
player1 = raw_input("Enter name(Player 1):")
player2 = raw_input("Enter name(Player 2):")

##Settings
#Stones in the Pile
pile = 2
while pile <= 2:
    pile = int(raw_input("Number of stones in the pile: "))
#Max Stones
maxStones = 1
while maxstones <= 1 or maxstones >= (pile - 1):
    maxstones = int(input("Maximum number of stones taken (suggested 5): "))

##Messages
message1 = "Invalid number of stones."
message2 = "Not enough stones."
message3 = "No stones left. " + player1 + " wins!"
message4 = "No Stones left. " + player2 + " wins!"


##Taking stones
turn1 = True
while pile > 0:
    if turn1 == True:
        pick = int(raw_input(str(pile) + " stones left. " + player1 + ", pick 1-" + str(maxStones) + " stones:"))
        if pick > maxStones or pick < 1:
            print message1
        elif pick > pile:
            print message2
        else:
            pile = (pile-pick)
            turn1 = False

    if turn1 == False and pile != 0:    #For some reason, the != 0 is needed
        pick= int(raw_input(str(pile) + " stones left. " + player2 + ", pick 1-" + str(maxStones) + " stones:"))
        if pick > maxStones or pick < 1:
            print message1
        elif pick > pile:
            print message2
        else:
            pile = (pile-pick)
            turn1 = True

##Victory
if pile == 0 and turn1 == True:
    print message3
elif pile == 0:
    print message4

