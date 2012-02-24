#!/usr/bin/python env

# Calculate if a point is within a box
#
# I think a few of the point checks are flawed in the unit testing. I highlighted them, after graphing them out on paper.
#
#True = In Range
#False = Out of range
#inx/iny = input x / input y

def point_in_box((inx, iny), (x,y,w,h)):
    if inx > (x + w) or inx < x:
        return False

    elif iny < (y - w) or iny > y:
        return False
    
    elif inx == x and iny == y:
        return True

    else:
        return True


#Tests
box = (10,10,10,10)
print point_in_box((0,0), box), "F"
print point_in_box((15,0), box), "F" #Shouldn't this be T?
print point_in_box((25,0), box), "F"
print point_in_box((0,15), box), "F"
print point_in_box((15,15), box), "T"  #Shouldn't this be F?
print point_in_box((25,15), box), "F"
print point_in_box((0,30), box), "F"
print point_in_box((15,30), box), "F"
print point_in_box((25,30), box), "F"

print point_in_box((10,10),box), "T"
print point_in_box((10,15),box), "T" # Shouldn't this be F?
print point_in_box((15,10),box), "T"
print point_in_box((20,20),box), "F"
print point_in_box((20,15),box), "F"
print point_in_box((15,20),box), "F"
