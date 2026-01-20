#Name:Ivan Gomez
#Class: 5th Hour
#Assignment: HW17
import random
#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
def restart():
    replay = int(input("1 for Replay and 2 for Quit?"))

    if replay == 1:
        RPS()
    else:
        quit()




def RPS():
    player = int(input("1 for rock, 2 for paper, 3 for scissor"))
    opponent = random.randint(1,3)

    if player == opponent:
        print("both draw!")

    #Lose Statements / rock - paper / paper - scissors / scissors - rock
    elif player == 1 and opponent == 2:
        print("you choose rock and opponent choose paper you lose")

    elif player == 2 and opponent == 3:
        print("you choose paper and opponent choose scissors you lose")

    elif player == 3 and opponent == 1:
        print("you choose scissors and opponent choose rock you lose")

    # Win Statements
    elif player == 2 and opponent == 1:
        print("you choose paper and opponent choose rock you win")

    elif player == 3 and opponent == 2:
        print("you choose scissors and opponent choose paper you win")

    elif player == 1 and opponent == 3:
        print("you choose rock and opponent choose scissors you win")
    restart()
RPS()
#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.