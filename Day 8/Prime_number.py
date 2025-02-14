def prime_checker(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print("This is a prime number.")
    else:
        print("This is not a prime number.")      

number = int(input("Write the number:-\n"))
prime_checker(number)