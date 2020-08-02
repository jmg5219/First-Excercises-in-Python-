num_list = [-2,-1,0,1,2]#input list
pos_nums = []#resultant list to store positive numbers
j = 0
for i in range(0,len(num_list)):#cycling through the elements of the input list
    if num_list[i] > 0:#if the element is positive we store it in the resultant list
        pos_nums.append(num_list[i])

for j in range(0,len(pos_nums)):#printing the elements in the resultant list
    print(pos_nums[j])

        