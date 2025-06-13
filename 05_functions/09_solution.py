num = int(input("Enter a Number: "))
def even_num(num):
    for number in range(1, num + 1):
        if number%2==0:
            yield number
print(f"Even numbers from 1 to {num} are:", list(even_num(num)))
