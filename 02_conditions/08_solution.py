# 08 Password Strength Checker: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

while True:
    password = input("Enter a Password: ")
    if len(password) == 0:
        print("Password cannot be empty. Please enter a password.")
    else:
        break

if len(password) < 6:
    print("Your Password is Weak")
elif 6 <= len(password) <= 10:
    print("Your Password is Medium")
else:
    print("Your Password is Strong")