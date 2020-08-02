arr1 = [2,4,5]#input vectors
arr2 = [2,3,6]
arr3 = []#resultant vector

for i in range(0,len(arr1)):
    arr3.append(arr1[i]*arr2[i])#appending the result to new vector
    print(arr3[i])#printing the new vector