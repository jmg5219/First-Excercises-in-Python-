num_list = [1,2,3]#input list
factor = 2#input factor
new_list = []#new list to store result

for i in range(0,len(num_list)):#cycling through the elements in the input list
    new_list.append(num_list[i]*factor)#appending the result of multiplication in the new list
print(new_list)#printing the new list

