num = int(input("Enter a Number: "))
isPrime = True

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break  
    if isPrime:
        print(f"{num} is a Prime Number")
    else:
        print(f"{num} is Not a Prime Number")
else:
    print("Number should be greater than 1")