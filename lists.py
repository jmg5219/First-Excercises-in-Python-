power_rangers = ["Jason","Trini","Billy","Zack","Kim"]

# Looping through a list with the for loop
for i in range (0,len(power_rangers)) : 
    print(power_rangers[i])
print ()

# More looping through a list with the for loop
for ranger in power_rangers:
    if ranger == "Billy":
        print(ranger)
        break# this is a break in the control structure useful for finding things
    else:
        print('This ranger is not Billy')
print()#printing a line break in python

# Looping through a list with the while loop
i = 0 
while i < len(power_rangers):
    print(power_rangers[i])
    i += 1
print()

#Creating another list using append
another_list = []
another_list.append("Jason")
another_list.append("Trini")
another_list.append("Billy")
another_list.append("Zack")
another_list.append("Kim")

# Looping through another list with the while loop
i = 0 
while i < len(another_list):
    print(another_list[i])
    i += 1
print()


another_list.append("Tommy")

# Looping through another list with the while loop
i = 0 
while i < len(another_list):
    print(another_list[i])
    i += 1
print()

# removing from the list 
another_list.remove("Tommy")

# Looping through another list with the while loop
i = 0 
while i < len(another_list):
    print(another_list[i])
    i += 1
print()