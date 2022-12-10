import random

user_wins = 0
computer_wins = 0
result = ["rock", "paper", "scissors"]
while True:
  User_input = input(
    'Play Your Move: Rock/Paper/Scissors or Q to Quit: ').lower()
  if User_input == "q":
    break
  if User_input not in result:
    print("Invalid Input")
    continue
  random_number = random.randint(0, 2)
  computer_input = result[random_number]
  if computer_input == User_input:
    print('Draw')
    continue
  elif computer_input == "paper" and User_input == "scissors":
    print("User Wins")
    user_wins = user_wins + 1
    continue
  elif computer_input == "scissors" and User_input == "rock":
    print("User Wins")
    user_wins = user_wins + 1
    continue
  elif computer_input == "rock" and User_input == "paper":
    print("User Wins")
    user_wins = user_wins + 1
    continue
  else:
    print("Computer Wins")
    user_wins = user_wins + 1
    continue

print(f'User won {user_wins} Times, Computer won {computer_wins} Times')
