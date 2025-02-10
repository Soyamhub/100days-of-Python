Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

import random

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
value = [Rock, Paper, Scissor]
random_value = random.randint(0,2)
user_sign = value[user]
computer_sign = value[random_value]
print(f"Your SIgn\n{user_sign}")
print(f"Computer SIgn\n{computer_sign}")
if user_sign == Paper and computer_sign == Rock:
    print("You Win!")
elif user_sign == Rock and computer_sign == Scissor:
    print("You Win!")
elif user_sign == Scissor and computer_sign == Paper:
    print("You Win!")
elif user_sign == computer_sign:
    print("Draw!")
else:
    print("You Lose!")             