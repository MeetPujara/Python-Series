# 02 Movie Ticket Pricing: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("Enter Age: "))
childrenTicketPrice = 8
adultTicketPrice = 12
discount = 2

if(age<18):
    print(f"You are a Child, Your Ticket Price is {childrenTicketPrice}$")
    day = input("Enter Day: ")
    if day == "Wednesday":
        print(f"Yay, Today is Wednesday, You got a Discount of ${discount} and Now,You have to pay {childrenTicketPrice-discount}$")
    else:
        print("No Discount Today")
elif age>=18:
    print(f"You are an Adult, Your Ticket Price is {adultTicketPrice}$")
    day = input("Enter Day: ")
    if day == "Wednesday":
        print(f"Yay, Today is Wednesday, You got a Discount of {discount}$ and Now,You have to pay {adultTicketPrice-discount}$")
    else:
        print("No Discount Today")
