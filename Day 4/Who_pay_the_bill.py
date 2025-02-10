import random
names = input("Enter the name with a comma and space\n").split(", ")
lenght = len(names)
random_number = random.randint(0,lenght-1)
print(names[random_number])