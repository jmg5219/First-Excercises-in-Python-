mat_1 = [[1,3],[2,4]]
mat_2 = [[5,2],[1,0]]

mat_3 = [[0,0],[0,0]]

for i in range(len(mat_1)):
    for j in range(len(mat_2)):
        mat_3[i][j] = mat_1[i][j]+mat_2[i][j]
print(mat_3)


        

