import random

def card_deal(player, times):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for i in range(times):
        card = random.choice(cards)
        if score(player) > 21 and card == 11:
            player.append(1)
        else:
            player.append(card)
    return player    
    
def is_blackjack(cards_list):
    return sorted(cards_list) == [10, 11]
    
def winner(user, computer):
    user_score = score(user)
    comp_score = score(computer)

    if is_blackjack(user) and is_blackjack(computer):
        print("It's a Draw! Both have Blackjack.")
    elif is_blackjack(user):
        print("User Wins with a Blackjack!")
    elif is_blackjack(computer):
        print("Computer Wins with a Blackjack!")
    elif user_score > 21:
        print("User Busts! Computer Wins.")
    elif comp_score > 21:
        print("Computer Busts! User Wins.")
    elif user_score > comp_score:
        print("User Wins!")
    elif comp_score > user_score:
        print("Computer Wins!")
    else:
        print("It's a Draw!")

def score(cards_list):
    return sum(cards_list)
    
user = []
computer = []
     
user = card_deal(user, 2)
computer = card_deal(computer, 2)

print(user)
print(computer)

winner(user, computer)  


