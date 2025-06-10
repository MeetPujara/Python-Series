# 07 Coffee Customization: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

size = input("Enter The Coffee Cup Size(Small,Medium,Large): ").strip().capitalize()

if size in ["Small","Medium","Large"]:
    extraShot = input("Do you need Extra Shot of Espresso? (yes/no): ").strip().lower()
    if extraShot == "yes":
        print("Added Extra Shot of Espresso")
    else:
        print("No Problem Sir, Here's Your Coffee")
else:
    print("Invalid size entered. Please choose Small, Medium, or Large.")