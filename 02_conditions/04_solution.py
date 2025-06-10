# 04 Fruit Ripeness Checker: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = input("Enter Any Fruit: ")

if fruit:
    color = input("Enter the color of fruit: ")
    if(color == "Green"):
        print(f"{fruit} is Unripe")
    elif(color == "Yellow"):
        print(f"{fruit} is Ripe")
    elif(color == "Brown"):
        print(f"{fruit} is Overripe")