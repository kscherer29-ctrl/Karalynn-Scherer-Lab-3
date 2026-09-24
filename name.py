# Function that adds two numbers 
def add(x,y):
    print(x+y)

 # Function that substracts two numbers 
def subtract(x,y):
    print(x-y)

# Function that multiplies two numbers 
def multiply(x,y):
    print(x*y)

# Function that divides two numbers 
def divide(x,y):
    print(x/y)

###########################################################
######################Start of program#####################

while(True):
    print("Welcome to mah awesome calc app!!!")
    print("What would you like to do?")
    print("Type (a)dd (s)ubtract (m)ultiply (d)ivide (e)aster egg (q)uit")

    user_choice = input(": ")

    if user_choice == 'q':
        print("Shutting down")
        break

    if user_choice == 'e':
        guess = float(input("Guess the easter egg number: "))
        if guess == 9.75:
            print("Off to Hogwarts!!!🦉🪄🌟🏆")
    


    x = float(input("Enter your first number: "))
    y = float(input("Enter your second number: "))

    if user_choice == 'a':
        add(x,y)

    elif user_choice == 's':
        subtract(x,y)

    elif user_choice == 'm':
        multiply(x,y)

    elif user_choice == 'd':
        divide(x,y)

    else:
        print("Invalid choice")6