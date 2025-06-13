num = int(input("Enter a Number: "))

def factorial_output(num):
    factorial = 1
    while num>0:
        factorial *= num
        num -= 1
    return factorial

print(f"The Factorial of {num} is: ",factorial_output(num))