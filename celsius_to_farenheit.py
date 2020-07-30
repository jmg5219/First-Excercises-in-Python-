# try:
#     temp_c = int(input("Temperature in C?"))
#     temp_f = (temp_c*(9/5))+32
#     print("%.1f F" % (temp_f))
# except:
#     print('please verify numeric input and try again')


def convert_F(temp_c):
    temp_f = (temp_c*(9/5))+32
    return temp_f
    

temp_c = int(input("Temperature in C?"))

print("%.1f F" % (convert_F(temp_c)))
