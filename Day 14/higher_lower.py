import game_data
import art
import random

print(art.logo)

def check_winner(ans):
    if ans == 'A':
        if person1['follower_count'] > person2['follower_count']:
            return 1
        else:
            return 0 
    if ans == 'B':
        if person2['follower_count'] > person1['follower_count']:
            return 1
        else:
            return 0    

person1 = random.choice(game_data.data)
while(True):
    person2 = random.choice(game_data.data)
    if person1['name'] != person2['name']:
        break

print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}")

print(art.vs)

print(f"Compare B: {person2['name']}, a {person2['description']}, from {person2['country']}")

ans = input("Who has more followers? Type 'A' or 'B': ").upper()
winner = check_winner(ans)

if winner == 1:
    print("You win the game")
else:
    print("You lose the game")    
   