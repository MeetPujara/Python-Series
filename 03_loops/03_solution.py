table = int(input("Enter Table No: "))

for i in range(1,11):
    if i==5:
        continue
    print(f"{table} X {i} = {table*i}")
    