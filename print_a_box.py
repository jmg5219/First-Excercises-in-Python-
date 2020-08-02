width = int(input("Width?"))#prompting user for input on the width of the box
height = int(input("Height?"))#prompting user for input on the height of the box

i = height#initializing incrementors
j = width   
for i in range(1, i+1) : #cycling through row
    for j in range(1, j+1) : #cycling through column
        if (i==1 or i==height or j==1 or j==width):#if at the ends of the box we print
            print("*", end="")  # appending a space after print if at the ends of the box 
        else :
            print(" ", end="") #printing a blank space if in inside the box               
    print() 

  