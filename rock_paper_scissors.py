import  random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", 'paper', "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game ended")
        exit = True
    elif user_input == "rock":
        if computer_input == "rock":
            print("your input is rock")
            print("the computer input is rock")
            print("its a tie")
        elif computer_input == "paper":
            print("your input is rock")
            print("the computer input is paper")
            print("you lose")
            computer_points +=1
        elif computer_input == "scissors":
            print("your input is rock")
            print("the computer input is scissors")
            print("you win")
            user_points +=1
    elif user_input == "paper":
        if computer_input == "paper":
            print("your input is paper")
            print("the computer input is paper")
            print("its a tie")
        elif computer_input == "scissors":
            print("your input is paper")
            print("the computer input is scissors")
            print("you lose")
            computer_points +=1
        elif computer_input == "rock":
            print("your input is paper")
            print("the computer input is rock")
            print("you win")
            user_points +=1 
    elif user_input == "scissors":
        if computer_input == "scissors":
            print("your input is scissors")
            print("the computer input is scissors")
            print("its a tie")
        elif computer_input == "rock":
            print("your input is scissors")
            print("the computer input is rock")
            print("you lose")
            computer_points +=1
        elif computer_input == "paper":
            print("your input is scissors")
            print("the computer input is paper")
            print("you win")
            user_points +=1 
    else:
        print("invalid input, try to type the right input")    
    print("your score is ", user_points)
    print("the computer score is: ", computer_points)                      