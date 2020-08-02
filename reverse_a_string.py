num_list = [1,2,3]#input list
factor = 2
new_list = []
test_stuff = "Jai"

for i in range(0,len(num_list)):#multiplying input list with a factor
    new_list.append(num_list[i]*factor)
print(new_list)

#reversing the list
new_list.reverse()#using the reverse method to reverse the string
print(new_list)

for letter in test_stuff:#more string reversal
    string_list.append(letter)
print(string_list)
string_list.reverse()
print(string_list)

new_string =" "
for letter in string_list:
    new_string += letter
print(new_string)

