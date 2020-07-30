def madlib(name,subject):
    the_madlib = "Your name is %s and your favorite subject is %s" % (name,subject)
    return the_madlib

print("Please fill in the blanks:")
print("____(name)____'s favorite subject in school is ____(subject)____.")
name = input("What is your name?")
subject = input("What is your favorite subject?")
print(madlib(name,subject))