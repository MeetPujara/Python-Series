items = ["apple", "banana", "orange", "apple", "mango"]

unique_items = set() #It does not allow repeated value

for item in items:
    if item in unique_items:
        print("Duplicate Item:",item)
        break
    unique_items.add(item)
