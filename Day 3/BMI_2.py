weight = float(input("Give the weight of a person (in kg)\n"))
height = float(input("Give the height of a person (in meter)\n"))
BMI = weight / (height * height)
if BMI < 18.5:
    print(f"Your BMI index is {BMI}, you are underweight.")
elif 18.5 < BMI < 25:
    print(f"Your BMI index is {BMI}, you have a normal weight.")
elif 25 < BMI < 30:
    print(f"Your BMI index is {BMI}, you are slightly overweight.")   
elif 30 < BMI < 35:
    print(f"Your BMI index is {BMI}, you are obese.")
else:
    print(f"Your BMI index is {BMI}, you are extremely obese.")        
        