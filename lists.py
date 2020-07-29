power_rangers = ["Jason","Trini","Billy","Zack","Kim"]
# Looping through a list with the for loop
for i in range (0,len(power_rangers)) : 
    print(power_rangers[i])

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