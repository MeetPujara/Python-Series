# 06 Transportation Mode Selection: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

transportation = int(input("Tell me the distance: "))

if transportation<3:
    print("Walk")
elif transportation>=3 and transportation<15:
    print("Go with The Bike")
elif transportation>=15:
    print("Go with The Car")