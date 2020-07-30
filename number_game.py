import random# importing random library
magic_number = random.randint(1,10)#generating a random number for the magic number user need to guess
user_input = 0#initializing variables
guess = 0 
total_guess = 5
remain_guess = total_guess - guess
play_again = 'Y'



while play_again == 'Y':#while loop to restart game if user chooses to
    if play_again == 'Y':#entry into the game body if restart selected
        remain_guess = total_guess - guess# calculating remaining guesses availble to user
        if remain_guess > 0 :#if user has remaining guesses allow user to choose a number
            print("I am thinking of a number between 1 and 10.")
            print(magic_number)
            guess += 1#incrementing the number of guesses attempted by user
            print('You have %d guesses left.' % (remain_guess))
            try:
                user_input = int(input("What's the number? "))#asking for user's guess
            except:
                print('Please enter a numeric value for your guess')#error handling in case user enters non numeric
            if user_input == magic_number:#win events
                print('Yes! You win!')
                print() 
                flag = 0#prompting user on  new game
                while flag == 0:               
                    play_again = input('Do you want to play again (Y or N)?')
                    if play_again == 'N' :
                        print('Bye!')
                        flag = 1
                    elif play_again == 'Y':
                        magic_number = random.randint(1,10)
                        total_guess = 5
                        guess = 0
                        flag = 1
            if user_input > magic_number :#loss events
                print ('Try a smaller number')
                print()
            if user_input < magic_number :
                print('Try a larger number')
                print()
        elif remain_guess == 0:
            flag = 0#prompting user on new game
            while flag == 0:               
                play_again = input('Do you want to play again (Y or N)?')
                if play_again == 'N' :
                    print('Bye!')
                    flag = 1
                elif play_again == 'Y':
                    magic_number = random.randint(1,10)
                    total_guess = 5
                    guess = 0
                    flag = 1
    elif play_again == 'N' :#exit events
        print('Bye!')
