while True:
    print("WEIGHT CONVERTER \n ")
    print("=" * 16)
    print("Convert weight from: ")
    print("1. Lbs")
    print("2. Kgs")
    choice = int(input("Enter 1/2 : "))

    try:
        if choice == 1: 
            old_weight = float(input("Enter weight in Lbs: "))
            bmi_weight = round(old_weight / 2.205, 2) 
            print(f"Weight = {bmi_weight} Kgs")

        elif choice == 2:
            bmi_weight = float(input("Enter weight in Kgs: "))
            new_weight = round(bmi_weight * 2.205, 2) 
            print(f"Weight = {new_weight} Lbs")

        else:
            print("Enter a valid choice, either 1 or 2.")

    except:
        print("Enter valid measurements!")

    print("HEIGHT CONVERTER")
    print("=" * 16)
    print("Convert height from: ")
    print("1. Feet")
    print("2. Cms")
    choice = int(input("Enter 1/2 : "))

    try:
        if choice == 1: 
            old_height = float(input("Enter height in Feet: "))
            new_height = round(old_height * 30.48, 2) 
            bmi_height = new_height / 100
            print(f"Height = {new_height} Cms")

        elif choice == 2:
            old_height = float(input("Enter height in Cms: "))
            bmi_height = old_height / 100
            new_height = round(old_height / 30.48, 2) 
            print(f"Height = {new_height} Feet")

        else:
            print("Enter a valid choice, either 1 or 2.")

    except:
        print("Enter valid measurements!")  

    print("BMI CALCULATOR")
    print("=" * 16)

    bmi = round(bmi_weight / pow(bmi_height, 2), 2)
    print(f"Youre BMI is: {bmi}")

    # Temperature Input
    temperature = input("What is your temperature? ")

    print(f"Your BMI is {bmi} and your temperature is {temperature}\u00b0C")

    cont = input("Do you want to continue (y/n)? ")
    if cont == "y":
        continue
    else:
        print("Goodbye!")
        break

