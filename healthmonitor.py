print("HEALTH MONITOR")
print("=" * 16)
name = input("Enter your name: ")

while True:
    print(f"Hello {name}. Which services do you need today?")
    print("1. Weight converter\n" \
          "2. Height converter\n" \
          "3. Health analysis")
    service = int(input("Enter your choice here(1, 2, 3): "))

    if service == 1:

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

    elif service == 2:
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

    elif service == 3:
        print("WEIGHT INPUT")
        print("=" * 16)
        print("Enter your weight in: ")
        print("1. Lbs")
        print("2. Kgs")
        choice = int(input("Enter 1/2 : "))
    
        try:
            if choice == 1: 
                old_weight = float(input("Enter weight in Lbs: "))
                bmi_weight = round(old_weight / 2.205, 2) 
                # print(f"Weight = {bmi_weight} Kgs")
    
            elif choice == 2:
                bmi_weight = float(input("Enter weight in Kgs: "))
                new_weight = round(bmi_weight * 2.205, 2) 
                # print(f"Weight = {new_weight} Lbs")
    
            else:
                print("Enter a valid choice, either 1 or 2.")
    
        except:
            print("Enter valid measurements!")
    
        print("HEIGHT INPUT")
        print("=" * 16)
        print("Enter your height in: ")
        print("1. Feet")
        print("2. Cms")
        choice = int(input("Enter 1/2 : "))
    
        try:
            if choice == 1: 
                old_height = float(input("Enter height in Feet: "))
                new_height = round(old_height * 30.48, 2) 
                bmi_height = new_height / 100
                # print(f"Height = {new_height} Cms")
    
            elif choice == 2:
                old_height = float(input("Enter height in Cms: "))
                bmi_height = old_height / 100
                new_height = round(old_height / 30.48, 2) 
                # print(f"Height = {new_height} Feet")
    
            else:
                print("Enter a valid choice, either 1 or 2.")
    
        except:
            print("Enter valid measurements!")  
    
        
        bmi = round(bmi_weight / pow(bmi_height, 2), 2)
        
    
        # Temperature Input
        temperature = float(input("What is your temperature? "))
    
        print("RESULTS")
        print("=" * 16)
        
    
        print(f"Your BMI is {bmi} and your temperature is {temperature}\u00b0C")
    
        if bmi < 18.5 :
            print("You are underweight")
        elif bmi > 24.9:
            print("You are overwight")
        else:
            print("You have healthy weight")
    
        if temperature < 36.1:
            print("Your temperature is dangerously low")
        elif temperature > 38:
            print("You have a fever")
        else:
            print("You are healthy")

    else:
        print("Enter a valid choice")
        




    
    cont = input("Do you want to continue (y/n)? ")
    if cont == "y":
        continue
    else:
        print(f"Goodbye {name}!")
        break

