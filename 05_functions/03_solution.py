num1 = input("Enter First Value: ")
num2 = input("Enter Second Value: ")

def multiply(a, b):
    if a.isdigit() and b.isdigit():
        return int(a) * int(b)
    elif a.isalpha() and b.isdigit():
        return a * int(b)
    elif b.isalpha() and a.isdigit():
        return b * int(a)
    else:
        return "Invalid input types."

result = multiply(num1, num2)
print(f"Multiply of {num1} and {num2} is: {result}")