import random, art
print(art.logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def game(level):
    for i in range(level,0,-1):
        print(f"You have {i} attempts to guess the number.")
        guess = int(input("Make a guess! "))
        if rand_num == guess:
            print(f"Guessed it right! The answer was {rand_num}")
            return
        elif guess > rand_num:
            print(f"Too high!")
        else:
            print(f"Too low!") 
        print("Guess Again!")
    print("Game Over!")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS



print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
rand_num = random.randint(1,100)
level = set_difficulty()
game(level)

 

  

           