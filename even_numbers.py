def even_nums(num_list):#Function to find even numbers from a list
    for i in range(0,len(num_list)):
        if (num_list[i] % 2) == 0:
            print(num_list[i])

num_list = [1,2,3,4,5,6,7,8,9,10]#Input list that includes even and odd numbers
even_nums(num_list)#calling function to find even numbers