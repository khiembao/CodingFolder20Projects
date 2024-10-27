def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))


def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))

def div(a,b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))

def mult(a,b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Division")
    print("D. Multiplication")
    print("E. Exit")

    choice = input("input your choice: ")
    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("insert your first number: "))
        b = int(input("insert your second number: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("insert your first number: "))
        b = int(input("insert your second number: "))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Division")
        a = int(input("insert your first number: "))
        b = int(input("insert your second number: "))
        div(a, b)
    elif choice == "d" or choice == "D":
        print("Multiplication")
        a = int(input("insert your first number: "))
        b = int(input("insert your second number: "))
        mult(a, b)
    elif choice == "e" or choice == "E":
        print("Good Bye")
        quit()
    else:
        print("wrong command, please insert again")    





