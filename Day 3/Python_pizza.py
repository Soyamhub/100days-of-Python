size = input("Which size pizza you want?(S,M,L)")
add_pepperoni = input("Do you want to add pepperoni ? (Y or N)(extra $2 for S and $3 for M and L)")
extra_cheese = input("Do you want to add extra cheese ?(Y or N)(extra $1)")
if size == 'S' or size == 's':
    bill = 15
    if add_pepperoni == 'Y' or add_pepperoni == 'y':
        bill += 2
    if extra_cheese == 'Y' or extra_cheese == 'y':
        bill += 1    
if size == 'M' or size == 'm':
    bill = 20
    if add_pepperoni == 'Y' or add_pepperoni == 'y':
        bill += 3
    if extra_cheese == 'Y' or extra_cheese == 'y':
        bill += 1  
if size == 'L' or size == 'l':
    bill = 25
    if add_pepperoni == 'Y' or add_pepperoni == 'y':
        bill += 3
    if extra_cheese == 'Y' or extra_cheese == 'y':
        bill += 1 
print("Thank you for choosing Python Pizza Deliveries:)")         
print(f"Your final bill is ${bill}")                        