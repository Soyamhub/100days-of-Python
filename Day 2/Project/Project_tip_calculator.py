#This is a tip calculator where you can calculate the total bill after adding the tip and split in your friends
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill ?\n"))
tip = float(input("How much tip would you like to give ? 10, 12, or 15 ?\n")) / 100
total_bill = bill + (bill * tip)
persons = float(input("How many people to split the bill ?\n"))
final_bill = round(total_bill / persons, 2)
print(f"Each person should pay: Rs.{final_bill}")
