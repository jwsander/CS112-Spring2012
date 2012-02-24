#!/usr/bin/env python

# Create a greeter

def greeter(name):
    if name == str(name):
        print "hello,", name.lower()
    elif name == int(name):
        print "hello,", name

#User Input (Optional):
#name = raw_input("What's your name?")
#greeter(name)



# Draw a box

def box(w,h):

    #Limitations
    if w == str(w) or h == str(h):
        print "Error: Invalid Dimensions"
    elif w != int(w) or h != int(h):
        print "Error: Invalid Dimensions"
    elif w <= 0 or h <= 0:
        print "Error: Invalid Dimensions"
    
    #Extra Variables
    else:
        listw = ["+"]
        listh = ["|"]
        row = ""
        space = ""
        
    #Last line
        thin_box = False
        if h < 2:
            thin_box = True
    
    #Changing width
        w -= 1
        while w > 1:
            listw.append("-")
            listh.append(" ")    #space in middle
            w -= 1
        if w == 1:
            listw.append("+")    #right corner
            listh.append("|")    #right side

    #Printing rows 
        for x in listw:
            row += str(x)
        for y in listh:
            space += str(y)
        print row
        
    #Changing length
        while h > 2:
            print space
            h -=1
        
    #Bottom line
        if len(listw) >= 1 and thin_box == False:
            print row
        
#User Input (Optional)
#usr_w = raw_input("Width of box: ")
#usr_h = raw_input("Height of box: ")
#box(usr_w,usr_h)

#Tests
box(1,1)
box(1,2)
box(1,3)
box(1,4)
box(2,1)
box(3,1)
box(4,1)
box(2,2)
box(2,3)
box(2,4)
box(3,2)
box(4,2)
box(3,3)
box(3,4)
box(4,3)
box(4,4)
        


