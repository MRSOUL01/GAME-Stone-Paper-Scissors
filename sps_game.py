"""Module
the start """
import random as rd 

#print statement
print("Welcome to the Rock, Paper, Scissors game!")
print("1. Stone")
print("2. Paper")
print("3. Scissors")

#Player
ch = int(input("Enter your choice (1-3): "))
try:
    if ch == 1:
        print("You chose Stone")
        player = 1
    elif ch == 2:
        print("You chose Paper")
        player = 2
    elif ch == 3:
        print("You chose Scissors")
        player = 3
except:
    print("choose the in the range of 1 of 3")

#Computer
computer = rd.randint(1, 3)

if computer == 1:
    print("Computer chose Stone")
elif computer == 2:
    print("Computer chose Paper")
elif computer == 3:
    print("Computer chose Scissors")

# use of def 
def wn():
    print("you win!")

def ln():
    print("you lose!")

# Compare
if player == computer:
    print("It's a tie!")   
    print(player)
    print(computer)
elif player == 1 and computer == 3:
    print(" Stone beats Scirror")
    wn()
elif player == 1 and computer == 2:
    print(" Paper beats Stone")
    ln()
elif player == 2 and computer == 1:
    print(" Paper beats Stone")
    wn()
elif player == 2 and computer == 3:
    print(" Scissors beats Paper")
    ln()
elif player == 3 and computer == 1:
    print(" Stone beats Scissors")
    wn()
elif player == 3 and computer == 2:
    print(" Scissors beats Paper")
    ln()
    
# the End 
print("Try again.")
