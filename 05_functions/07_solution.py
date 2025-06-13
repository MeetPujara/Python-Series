def sum(*numbers):
    result = 0
    for num in  numbers:
        result += num
    return result

num_list =[]
while True:
    numbers = input("Enter a Number: ")
    if numbers == "":
        break
    else:
        numbers = int(numbers)
        num_list.append(numbers)
print(f"The Sum of {num_list}: ",sum(*num_list))

        