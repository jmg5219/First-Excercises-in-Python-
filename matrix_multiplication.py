# 2x2 matrix multiplication
mat_1 = [[1,2],[0,3]]
mat_2 = [[6,4],[7,5]]

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

mat_3 = emp_mat(mat_1)#calling function and creating an empty matrix for the result


if mat_size(mat_1) == mat_size(mat_2) :#adding matrix if both are the same size
    for i in range(0,len(mat_1)):
        for j in range(0,len(mat_2)):
            mat_3[0][0] = (mat_1[0][0]*mat_2[0][0])+(mat_1[0][1]*mat_2[1][0])
            mat_3[0][1] = (mat_1[0][0]*mat_2[0][1])+(mat_1[0][1]*mat_2[1][1])
            mat_3[1][0] = (mat_1[1][0]*mat_2[0][0])+(mat_1[1][1]*mat_2[1][0])
            mat_3[1][1] = (mat_1[1][0]*mat_2[0][1])+(mat_1[1][1]*mat_2[1][1])
            

print(mat_3)