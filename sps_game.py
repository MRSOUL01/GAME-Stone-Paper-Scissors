import random as rd

print("Welcome to the Rock, Paper, Scissors game!")
print("1. Stone")
print("2. Paper")
print("3. Scissors")

ch = int(input("Enter your choice (1-3): "))

if ch == 1:
    print("You chose Stone")
    player = 1
elif ch == 2:
    print("You chose Paper")
    player = 2
elif ch == 3:
    print("You chose Scissors")
    player = 3
else:
    print("Invalid choice. Please enter a number between 1 and 3.")

computer = rd.randint(1, 3)

if computer == 1:
    print("Computer chose Stone")
elif computer == 2:
    print("Computer chose Paper")
elif computer == 3:
    print("Computer chose Scissors")

if player == computer:
    print("It's a tie!")
elif player == 1 and computer == 3:
    print("You win! Stone crushes Scissors.")
elif player == 1 and computer == 2:
    print("You lose! Paper covers Stone.")
elif player == 2 and computer == 1:
    print("You win! Paper covers Stone.")
elif player == 2 and computer == 3:
    print("You lose! Scissors cut Paper.")
elif player == 3 and computer == 1:
    print("You lose! Stone crushes Scissors.")
elif player == 3 and computer == 2:
    print("You win! Scissors cut Paper.")