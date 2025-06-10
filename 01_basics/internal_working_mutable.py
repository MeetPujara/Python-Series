# Example 1: Assigning by reference (both variables point to the same list)
l1 = [1, 2, 3]
l2 = l1  

l2 = [1, 2, 3]  # l2 now refers to a new list, l1 is unchanged

l1[0] = 33  
# print("L1 is: ", l1)
# print("L2 is: ", l2)


# Example 2: Both variables refer to the same list (reference assignment)
p1 = [1, 2, 3]
p2 = p1 

p1[0] = 33 

# print("P1 is: ", p1)
# print("P2 is: ", p2)

# Example 3: Creating a copy using slicing ([:] creates a new list)
h1 = [1, 2, 3]
h2 = h1[:]  # h2 is a new list with the same elements as h1

# print("H1 is: ",h1)
# print("H2 is: ",h2)

# Example 4: Demonstrating 'is' (identity) vs '==' (equality)

list_a = [1, 2, 3]
list_b = list_a  # list_b refers to the same object as list_a

list_a = [1, 2, 3]  # list_a now refers to a new list object

print(list_a == list_b)   # True: both lists have the same contents
print(list_a is list_b)   # False: they are different objects in memory