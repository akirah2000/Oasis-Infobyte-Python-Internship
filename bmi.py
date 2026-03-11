try:
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))

    bmi = weight / (height * height)
    bmi = round(bmi, 2)

    print("Your BMI is:", bmi)

    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")

except:
    print("Invalid input. Please enter numbers only.")
