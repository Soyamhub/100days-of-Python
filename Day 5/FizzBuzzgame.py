#Fizz buzz is a group word game for children to teach them about division. Players take turns to count incrementally, replacing any number divisible by three with the word “fizz”, and any number divisible by five with the word “buzz”. Play. Players generally sit in a circle.
for i in range(1,101):
    if i % 3 == 0  and i % 5 == 0:
        print("FizzBuzz")  
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")    
    else:
        print(i)    