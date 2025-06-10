# 10. Pet Food Recommendation: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

species = input("Enter Species: ")
age = int(input("Enter Age: "))

if species == "Dog" and age < 2:
    print("Puppy Food")
elif species == "Dog" and age >= 2 and age <= 7:
    print("Adult Dog Food")
elif species == "Dog" and age > 7:
    print("Senior Dog Food")
elif species == "Cat" and age <= 2:
    print("Kitten Food")
elif species == "Cat" and 2 < age <= 5:
    print("Adult Cat Food")
elif species == "Cat" and age > 5:
    print("Senior Cat Food")
else:
    print("No recommendation available for this species or age.")