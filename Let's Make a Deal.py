import random

## defining the door class
class Door():
    def __init__(self, prize):
        self.prize = prize
        self.is_opened = False

    def open_door(self):
        self.is_opened = True

    def __repr__(self):
        return f"Door({self.prize})"

## Function to initialize the game with one car and two goats
def initialize_game():
    prizes = ['Goat', 'Goat', 'Car']
    random.shuffle(prizes)
    doors = [Door(prize) for prize in prizes]
    return doors

## Function to simulate the player's first choice
def make_first_choice():
    print("Choose a door (1, 2, 3):")
    choice = int(input()) - 1
    return choice

## Function to reveal a goat behind a door that wasn't chosen
def reveal_goat(doors, first_choice):
    for i, door in enumerate(doors):
        if i != first_choice and door.prize == 'Goat':
            door.open_door()
            print(f"Door {i + 1} has a Goat behind it.")

## Function to offer the player a chance to switch their choice
def offer_switch(doors, first_choice):
    print("Do you want to switch your choice? (Yes/No):")
    decision = input().lower()
    if decision == 'yes':
        for i, door in enumerate(doors):
            if i != first_choice and not door.is_opened:
                return i
    return first_choice

## Function to check if the player's choice has the car
def check_win(doors, choice):
  return doors[choice].prize == 'Car'

## Main game loop
def play_game():
  wins = 0
  games = 0

  while True:
    doors = initialize_game()
    first_choice = make_first_choice(doors)
    reveal_goat(doors, first_choice)
    final_choice = offer_switch(doors, first_choice)
    if check_win(doors, final_choice):
      print("You got a goat")
      wins += 1
      games += 1
    else:
      print("You got a car")
      games += 1

    print("Do you want to play agian? (Yes/No): ")
    if input().lower() != 'Yes':
      break
  print(f"Total wins: {wins} out of {games} games! ")

## Starting the game
if __name__ == "__main__":
  play_game()