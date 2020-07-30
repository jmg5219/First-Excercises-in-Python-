# try:
#     temp_c = int(input("Temperature in C?"))
#     temp_f = (temp_c*(9/5))+32
#     print("%.1f F" % (temp_f))
# except:
#     print('please verify numeric input and try again')


def convert_c(temp_f):
    temp_c = (temp_f-32)*(5/9)
    return temp_c
    

temp_f = int(input("Temperature in F?"))
print("%.1f C" % (convert_c(temp_f)))