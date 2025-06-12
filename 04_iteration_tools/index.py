print("Welcome,Let's Understand File")
chai = "Lemon Tea"
print(chai)
print("Lets Go")
print("File Handling")

# ✅ Opening a file named index.py (Make sure this file exists in your folder)
# f = open('index.py')

# ✅ Reads the first line of the file (if used)
# f.readline()

# ✅ List is an Iterable, so we can loop over it
myList = [1, 2, 3, 4]

# ✅ Convert the list into an Iterator using iter()
I = iter(myList)
# print(I)                 # Shows it's an iterator object
# print(I.__next__())      # OR use next(I) — gives 1st item

# ✅ Files are already Iterators
f = open('index.py')
print(iter(f) is f)  # ✅ True: because file objects already support __next__()

# ✅ So we can directly use next(f) to read one line at a time
# next(f)

# ✅ Lists are Iterables but NOT Iterators
myNewList = [1, 2, 3]
print(iter(myNewList) is myNewList)  # ❌ False — list needs to be converted to iterator

# ✅ Dictionary iteration
D = {'a': 1, 'b': 2}
for key in D.keys():
    print(key)  # ✅ Iterating over keys using for loop

# ✅ Getting an iterator from a dictionary
I = iter(D)
print(I)  # Shows it's a dict_keyiterator

# ✅ Dictionary itself is not an iterator
print(iter(D) is D)  # ❌ False

# ✅ Range is also Iterable
R = range(0, 5)
R1 = iter(R)        # Converting range to iterator
print(next(R1))     # ✅ Works: prints 0
