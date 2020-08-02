#Defining a function to convert temperature in Centigrade to Fahrenheit
def convert_F(temp_c):
    temp_f = (temp_c*(9/5))+32
    return temp_f
    
#Prompting User Input fo rTemperature in Centigrade
temp_c = int(input("Temperature in C?"))
#Using string interpolation to print the units
print("%.1f F" % (convert_F(temp_c)))#Calling the function to perform the conversion 


