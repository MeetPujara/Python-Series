# 03 Grade Calculator:Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

marks = int(input("Enter Marks: "))

if marks>=90 and marks<=100:
    print("A Grade")
elif marks>=80 and marks<=89:
    print("B Grade")
elif marks>=70 and marks<=79:
    print("C Grade")
elif marks>=60 and marks<=69:
    print("D Grade")
else:
    print("Fail")