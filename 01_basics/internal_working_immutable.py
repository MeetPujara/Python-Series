# Example1: Strings are immutable in Python
username = "Meet"      # A string object "Meet" is created in memory.The variable 'username' now refers to this object.

# print(username)        

username = "DK"        # A new string object "DK" is created in memory. # The variable 'username' is updated to refer to "DK". The original "Meet" string object is unchanged (and may be garbage collected if unreferenced).

# print(username)        # Prints "DK"


# Example2: Integers are immutable in Python
x = 10         # An integer object 10 is created in memory. 'x' refers to this object.
y = x          # 'y' now also refers to the same integer object 10.

x = 15         # A new integer object 15 is created. 'x' is updated to refer to 15.
               # 'y' still refers to the original integer object 10.

print("X is: ", x) #X is: 15
print("Y is: ", y) #Y is: 10