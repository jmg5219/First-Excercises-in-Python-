def convert_c(temp_f):#Function to calculate temperature in Centigrade given input in Fahrenheit
    temp_c = (temp_f-32)*(5/9)
    return temp_c
    

temp_f = int(input("Temperature in F?"))#User prompt for temperature in Fahrenheit
print("%.1f C" % (convert_c(temp_f)))#Using string interpolation to print, result from called function