# 01 Age Group Categorization:-Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

age = int(input("Enter Age: "))

if age<13:
    print("You are Child")
elif age>=13 and age<=19:
    print("You are Teenager")
elif age>=20 and age<=59:
    print("You are Adult")
elif age>=60:
    print("You are Senior Citizen")
else:
    print("Enter Number")