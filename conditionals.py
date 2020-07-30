import random
magic_number = random.randint(1,10)
user_input = 0
guess = 0 
total_guess = 5
remain_guess = total_guess - guess
play_again = 'Y'


while play_again == 'Y':
    if play_again == 'Y':
        remain_guess = total_guess - guess
        if remain_guess > 0 :
            print("I am thinking of a number between 1 and 10.")
            #print(magic_number)
            guess += 1
            print('You have %d guesses left.' % (remain_guess))
            try:
                user_input = int(input("What's the number? "))
            except:
                print('Please enter a numeric value for your guess')
            if user_input == magic_number:
                print('Yes! You win!')
                print()
                play_again = input('Do you want to play again (Y or N)?')
                if play_again == 'N' :
                    print('Bye!')
                if play_again == 'Y':
                    total_guess = 5
                    guess = 0
            if user_input > magic_number :
                print ('Try a smaller number')
                print()
            if user_input < magic_number :
                print('Try a larger number')
                print()
        elif remain_guess == 0:
            play_again = input('Do you want to play again (Y or N)?')
            if play_again == 'N' :
                print('Bye!')
            if play_again == 'Y':
                total_guess = 5
                guess = 0
                remain_guess = total_guess - guess
    elif play_again == 'N' :
        print('Bye!')
