import os, time
import art
print(art.logo)
again = True
bid_list = {}
while again:
    name = input("Enter your name: ")
    bid_price = int(input("Enter your bid amount: "))
    bid_list[name] = bid_price
    new_bid = input("Are there others who wants to bid?(yes or no)\n").lower()
    if new_bid == "no":
        again = False 
    else: 
        os.system('cls' if os.name == 'nt' else 'clear')       

os.system('cls' if os.name == 'nt' else 'clear')
max = 0
winner = ''
for name in bid_list:
    if bid_list[name] > max:
        max = bid_list[name]
        winner = name

print(f"The winner is {winner}")             