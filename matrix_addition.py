mat_1 = [[1,3],[2,4]]#specifying a matrix
mat_2 = [[5,2],[1,0]]

mat_3 = [[0,0],[0,0]]#specifying a resulting matrix to store

for i in range(len(mat_1)):#cycling through rows 
    for j in range(len(mat_2)):#cycling through columns
        mat_3[i][j] = mat_1[i][j]+mat_2[i][j]#performing matrix addition
print(mat_3)#printing the resulting matrix


        

