num_list = [1,2,3]
factor = 2
new_list = []
test_stuff = "Jai"

for i in range(0,len(num_list)):
    new_list.append(num_list[i]*factor)
print(new_list)

#reversing the list
new_list.reverse()
print(new_list)

for letter in test_stuff:
    string_list.append(letter)
print(string_list)
string_list.reverse()
print(string_list)

new_string =" "
for letter in string_list:
    new_string += letter
print(new_string)

