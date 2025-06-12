num = int(input("Enter a Number: "))
num_even = 0
sum_even = 0

for i in range(1,num+1):
    if i%2==0:
        num_even += 1
        sum_even += i
print(f"The Total Number of Even Numbers in {num} is:", num_even)
print(f"The Sum of Even Numbers in {num} is:", sum_even)
