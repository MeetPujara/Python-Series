def circle(r,pi=3.14):
    a = pi * r * r
    c = 2 * pi * r
    return a,c

r = int(input("Enter Radius: "))
area,circumference = circle(r)

print("Area of Circle is: ",area)
print("Circumference of Circle is: ", circumference)
