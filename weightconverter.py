print("WEIGHT CONVERTER")
print("=" * 16)
print("Convert weight from: ")
print("1. Lbs")
print("2. Kgs")
choice = int(input("Enter 1/2 : "))

try:
    if choice == 1: 
        old_weight = float(input("Enter weight in Lbs: "))
        new_weight = round(old_weight / 2.205, 2) 
        print(f"Weight = {new_weight} Kgs")

    elif choice == 2:
        old_weight = float(input("Enter weight in Kgs: "))
        new_weight = round(old_weight * 2.205, 2) 
        print(f"Weight = {new_weight} Lbs")

    else:
        print("Enter a valid choice, either 1 or 2.")

except:
    print("Enter valid measurements!")