import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like you password to be? (insert number of characters) "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password) # this will convert the list to string in order to print

    print(password)

while True:
    option = input("Do you want to generate a password? (type Yes/No): ")

    if option == "Yes":
        generate_password()
    elif option == "No":
        print("Program ended")
        quit()
    else:
        print("invalid input, please input Yes or No.")
