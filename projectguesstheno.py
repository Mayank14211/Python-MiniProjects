import random
target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target : ")
    #To QUIT the game
    if(userChoice == "Quit"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Sucess : Correct guess.")
        break

    elif(userChoice < target):
        print("you entered is too small number, Please guess the bigger number")

    else:
        print("you entered is too big number, Please guess the smaller number")
print("---GAME OVER---")
    