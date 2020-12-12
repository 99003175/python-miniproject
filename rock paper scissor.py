import random
import sys

win = 0
loss = 0
tie = 0
print("\n \t\t\t\t ****** Rock Paper Scissors *****")


class rps:
    def __init__(self, UserMove, computerMove):
        self.UserMove = UserMove
        self.computerMove = computerMove
        self.win = 0
        self.loss = 0
        self.tie = 0

    def check_win(self):
        if self.UserMove == self.computerMove:
            print("It is tie:!")
            self.tie += 1
        elif self.UserMove == 'r' and self.computerMove == 's':
            print("You win!")
            self.win += 1
        elif self.UserMove == "p" and self.computerMove == 'r':
            self.win += 1
            print("You win!")
        elif self.UserMove == "s" and self.computerMove == 'p':
            self.win += 1
            print("You win!")
        elif self.UserMove == "r" and self.computerMove == 'p':
            self.loss += 1
            print("You Lose!")
        elif self.UserMove == "p" and self.computerMove == 's':
            self.loss += 1
            print("You Lose!")
        elif self.UserMove == "s" and self.computerMove == 'r':
            self.loss += 1
            print("You Lose!")


# Loop the main game.
while True:
    print("""Enter Your Move:
            r - rock
            p - paper
            s - scissors
            q - quit""")
    UserMove = input("\n Type one of r, p, s or q : ")
    if UserMove == 'q':
        sys.exit()   # Quit the program.
    # Display what the computer choice:
    randomNumber = random.randint(1, 3)

    # Let Computer Choose it's move.
    if randomNumber == 1:
        computerMove = 'r'
        print("Rock")

    elif randomNumber == 2:
        computerMove = 'p'
        print("Paper")

    elif randomNumber == 3:
        computerMove = 's'
        print("Scissors")
    winobject = rps(UserMove, computerMove)
    winobject.check_win()
    win = win + winobject.win
    loss = loss + winobject.loss
    tie = tie + winobject.tie
    print(f"Win: {win}\nLoss: {loss}\nTie: {tie}")


