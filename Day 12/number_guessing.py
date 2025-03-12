import random, art
print(art.logo)

rand_num = random.randint(1,100)
def hardLevel():
    for i in range(5,0,-1):
        print(f"You have {i} attempts to guess the number.")
        guess = int(input("Make a guess! "))
        if rand_num == guess:
            print(f"Guessed it right! The answer was {rand_num}")
            break
        elif guess > rand_num:
            print(f"Too high!")
            print("You")
        else:
            print(f"Too low!") 
        print("Guess Again!")      

def easyLevel():
    for i in range(10,0,-1):
        print(f"You have {i} attempts to guess the number.")
        guess = int(input("Make a guess! "))
        if rand_num == guess:
            print(f"Guessed it right! The answer was {rand_num}")
            break
        elif guess > rand_num:
            print(f"Too high!")
        else:
            print(f"Too low!")   
        print("Guess Again!")   

difficulty = input("Choose The difficulty! 'Easy' or 'Hard': ").lower()
if difficulty == 'hard':
    hardLevel()
else:
    easyLevel()    

  

           