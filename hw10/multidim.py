#!/usr/bin/env python
"""
multidim.py

Multidimensional Arrays
=========================================================
This section checks to make sure you can create, use, 
search, and manipulate a multidimensional array.
"""


# 1.  find_coins
#       find every coin (the number 1) in a givven room
#          room: a NxN grid which contains coins

#          returns: a list of the location of coind
#
#       Example:
#       0 0 0 1 0 0
#       0 0 1 0 0 0
#       0 0 0 0 1 0
#       0 0 0 0 0 0
# 
#       >>> find_coins(room)
#       [ [3, 0], [2, 1], [4, 2] ]
#      
def find_coins(room):
    "returns a list of every coin in the room"
    coinlocs = []
    k = 0
    for i in room:
        l = 0
        for j in i:
            if j == 1:
               coinlocs.append((l,k))
            l += 1
        k += 1
    return coinlocs

room = [[0,0,1,0],
        [0,0,1,1],
        [0,0,0,0],
        [1,0,1,0]]

find_coins(room)


# 2. distance_from_player
#      calculate the distance from the player for each 
#      square in a room.  Returns a new grid of given
#120      width and height where each square is the distance
#      from the player

import math
def distance_from_player(player_x, player_y, width, height):
    "calculates the distance of each square from the player"
    grid = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(0)
        grid.append(row)
    grid[player_x][player_y] = 0

    k = 0
    for x in grid:
        l = 0
        for y in x:
            dist = 0
            dist = math.sqrt((k-player_x)**2 + (l-player_y)**2)
            grid[k][l] = dist
            l += 1
        k += 1
    return grid
    
            

