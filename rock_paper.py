import numpy as np 
choices = ["rock", "paper", "scissors"]
def get_winner(player,ai):
    if player == ai:
        return "It's a tie!"
    elif (player == "rock" and ai == "scissors") or (player == "paper" and ai == "rock") or (player == "scissors" and ai == "paper"):
        return "You win!"
    else:
        return "You lost AI wins!"
player = input("Enter rock, paper or scissors: ")

if player not in choices:
    print("Invalid choice! Please choose rock, paper or scissors.")
ai = np.random.choice(choices)
results = get_winner(player,ai)
print(results)