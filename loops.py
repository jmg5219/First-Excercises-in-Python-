title = "Green Lantern Corp."
STOP = 10 
counter = 0 
#Prints Even Letters and no spaces
while counter < len(title):
    if (counter % 2) == 0 and title[counter] != ' ':
        print(title[counter])
    counter += 1

#Prints Odd Letters
# while counter < len(title):
#     if (counter % 2) != 0:
#         print(title[counter])
#         #print(counter)
#     counter += 1