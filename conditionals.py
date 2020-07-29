def number_game(magic_number):
    user_input = 0
    while user_input != magic_number:
        user_input = int(input("Guess a number 5-50: "))
        #print(magic_number)
        if user_input == magic_number:
            print("ARE YOU A MIND READER!?!?")
        elif (user_input > 50) or (user_input < 5):
            print("Guess was out of bounds")
        elif user_input < magic_number: 
            print("Sorry, try a higher number")
        elif user_input > magic_number:
            print("Sorry, try a lower number")

import random
magic_number = random.randint(5,50)
number_game(magic_number)