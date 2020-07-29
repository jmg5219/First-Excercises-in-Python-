coins = 0
print("you have %d coins." % (coins))
ask_coin = input("Do you want another?")

while ask_coin == 'yes':
    coins = coins + 1
    print("you have %d coins." % (coins))
    ask_coin = input("Do you want another?") 
else:
    print('Bye')
