name1 = input("Enter your name\n")
name2 = input("Enter their name\n")
print("Your love score is calculating....")
name1 = name1.lower()
name2 = name2.lower()
true_value = 0
love_value = 0
for i in name1 + name2: 
    if i in 'true':
        true_value += 1
    if i in 'love':
        love_value += 1        
true_love = int(str(true_value) + str(love_value))
if true_love < 10 and true_love > 90:
    print(f"Your love score is {true_love}, you are like coke and mentos.")
elif true_love > 40 and true_love < 50:    
    print(f"Your love score is {true_love}, you are already together.")
else:
    print(f"Your love score is {true_love}")    