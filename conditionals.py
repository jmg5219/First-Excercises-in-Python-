def number_game():
    user_input = int(input("Guess a number 5-50: "))
    magic_number = random.randint(5,50)
    print(magic_number)
    if user_input == magic_number:
        print("ARE YOU A MIND READER!?!?")
    elif (user_input > 50) or (user_input < 5):
        print("Guess was out of bounds")
    else: 
        print("Sorry, try again")

import random
number_game()