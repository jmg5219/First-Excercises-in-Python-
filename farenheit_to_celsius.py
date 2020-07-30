def convert_c(temp_f):
    temp_c = (temp_f-32)*(5/9)
    return temp_c
    

temp_f = int(input("Temperature in F?"))
print("%.1f C" % (convert_c(temp_f)))