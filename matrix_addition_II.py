def mat_size(mat_arg): #function to calculate matrix size
    rows = len(mat_arg)
    columns = len(mat_arg[0])
    mat_size = rows * columns
    return mat_size

def emp_mat(mat_arg):#function to create empty matrix
    rows = len(mat_arg)
    columns = len(mat_arg[0])
    emp_mat = [[0]*columns for i in range(columns)]
    return emp_mat


mat_1 = [[1,3,3],[2,4,4],[1,2,7]]#input matrix of any size
mat_2 = [[5,2,2],[1,0,6],[3,4,8]]#second matrix for addition must match size of 1st matrix
mat_3 = emp_mat(mat_1)#calling function and creating an empty matrix for the result



if mat_size(mat_1) == mat_size(mat_2) :#adding matrix if both are the same size
    for i in range(0,len(mat_1)):
        for j in range(0,len(mat_2)):
            mat_3[i][j] = mat_1[i][j] + mat_2[i][j]#cycling through matrix rows and columns and storing resultant matrix
else:
    print('Restart program, verify matrix 1 and matrix 2 have the same diemensions')#error handling in the event matrices are of different diemension
print(mat_3)#printing the matrices