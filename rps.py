import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = input("Choose (rock/paper/scissors): ").lower()

print(f"Computer chooses: {computer}")

if player == computer:
    print("Tie!")
elif (player == "rock" and computer == "scissors") or \
     (player == "scissors" and computer == "paper") or \
     (player == "paper" and computer == "rock"):
    print("You win!")
else:
    print("Computer wins!")