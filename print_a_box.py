width = int(input("Width?"))
height = int(input("Height?"))

i = height
j = width   
for i in range(1, i+1) : 
    for j in range(1, j+1) : 
        if (i==1 or i==height or j==1 or j==width):
            print("*", end="")   
        else :
            print(" ", end="")                
    print() 

  