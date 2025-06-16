# Python OOP Concepts (Q1 - Q10)
# Ready for GitHub Upload: Clean, Well-Structured, and Commented

# -----------------------------------------
# Q1. Basic Class and Object
# Create a Car class and instantiate it.
# -----------------------------------------
class PublicCar:
    def __init__(self, brand, model, battery_size):
        self.brand = brand
        self.model = model
        self.battery_size = battery_size

    def full_name(self):
        return f"My Car's brand is {self.brand} and model is {self.model}"

# Example (Public Access):
public_car = PublicCar("Ford", "Mustang", "N/A")
print("[Q1] Public Brand:", public_car.brand)
print("[Q1] Public Model:", public_car.model)
print("[Q1] Public Battery Size:", public_car.battery_size)
print("[Q1] Public Full Info:", public_car.full_name())


# -----------------------------------------
# Q2. Class Method and Self
# Already handled via full_name() above
# -----------------------------------------


# -----------------------------------------
# Q3. Inheritance | Q4. Encapsulation
# ElectricCar inherits from Car
# Car has private attributes with getter/setter
# -----------------------------------------
class Car:
    total_car = 0  # Q6. Class Variable

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def set_brand(self, new_brand):
        self.__brand = new_brand

    def set_model(self, new_model):
        self.__model = new_model

    def full_name(self):
        return f"My Car's brand is {self.__brand} and model is {self.__model}"

    def fuel_type(self):  # Q5. Polymorphism
        return "Petrol or Diesel"

    @staticmethod  # Q7. Static Method
    def general_description():
        return "Cars are used for transport and cars are amazing."

    @property  # Q8. Property Decorator
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):  # Q5. Polymorphism override
        return "Electric Charge"


# Instantiate and demonstrate behavior
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print("\n[Q4] Brand via Getter:", my_tesla.get_brand())
print("[Q4] Model via Getter:", my_tesla.get_model())
print("[Q3] Battery Size:", my_tesla.battery_size)
print("[Q2] Full Name:", my_tesla.full_name())
print("[Q5] Fuel Type:", my_tesla.fuel_type())

# Modify brand and model
my_tesla.set_brand("Audi")
my_tesla.set_model("R1")
print("[Q4] Updated Full Name:", my_tesla.full_name())

# Access static method
print("[Q7] Static Method (Class):", Car.general_description())
print("[Q7] Static Method (Instance):", my_tesla.general_description())

# Access class variable
print("[Q6] Total Cars Created:", Car.total_car)

# Property decorator usage
print("[Q8] Accessing Model (Read-Only Property):", my_tesla.model)


# -----------------------------------------
# Q9. isinstance() Checks
# -----------------------------------------
print("\n[Q9] Is my_tesla an instance of Car?", isinstance(my_tesla, Car))
print("[Q9] Is my_tesla an instance of ElectricCar?", isinstance(my_tesla, ElectricCar))


# -----------------------------------------
# Q10. Multiple Inheritance with Battery and Engine
# -----------------------------------------
class Battery:
    def battery_info(self):
        return "This car uses a lithium-ion battery."

class Engine:
    def engine_info(self):
        return "This car has an electric engine."

class MyElectricCarTwo(Car, Battery, Engine):
    pass

advanced_car = MyElectricCarTwo("Hyundai", "Ioniq 5")
print("\n[Q10] Battery Info:", advanced_car.battery_info())
print("[Q10] Engine Info:", advanced_car.engine_info())
