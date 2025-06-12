input_str = input("Enter a String: ")

for char in input_str:
    if input_str.count(char) == 1:
        print("First Non-Repeated Character is: ",char)
        break