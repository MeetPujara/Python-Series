def greet(name="Meet"):
    return "Good Morning", name

input_str = input("Enter Name: ")

if(input_str==""):
    empty_str = greet()
    print(empty_str)
else:
    result = greet(input_str)
    print(result)