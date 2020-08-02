coins = 0#intializing number of coins
print("you have %d coins." % (coins))#utilizing string interpolation to print string and int types
ask_coin = input("Do you want another?")#prompting user for input

while ask_coin == 'yes':#while user input is yes we iterate
    coins = coins + 1
    print("you have %d coins." % (coins))#string interpolation
    ask_coin = input("Do you want another?") #user prompt
else:
    print('Bye')#exit statement if user does not wish to continue
