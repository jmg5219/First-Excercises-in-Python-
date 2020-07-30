arr1 = [2,4,5]
arr2 = [2,3,6]
arr3 = []

# for i in arr1:
#     print(i)

for i in range(0,len(arr1)):
    arr3.append(arr1[i]*arr2[i])
    print(arr3[i])