def madlib(name,subject):#function that handles string interpolation and returns string
    the_madlib = "Your name is %s and your favorite subject is %s" % (name,subject)
    return the_madlib

print("Please fill in the blanks:")#printing an example for the user to fill in
print("____(name)____'s favorite subject in school is ____(subject)____.")
name = input("What is your name?")#prompting user for inputs
subject = input("What is your favorite subject?")
print(madlib(name,subject))#calling function and passing inputs to print