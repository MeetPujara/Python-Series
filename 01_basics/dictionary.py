chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
# print(chai_types)


# print(chai_types.get("Masala"))
# chai_types["Green"] = "Fresh"
# print(chai_types)


# 1st way of printing dictionaries
# for chai in chai_types:
    # print(chai, chai_types[chai])
    
# 2nd way of printing
# for key,value in chai_types.items():
#     print(key,value)
#     # print(key,value,end=", ")

# if "Masala" in chai_types:
#     print("I have Masala")
# else:
#     print("I dont have Masala")

chai_types["Earl Grey"] = "Citrus"
# print(chai_types)

chai_types.pop("Green")
# print(chai_types)

chai_types.popitem()
# print(chai_types)

del chai_types["Ginger"]
# print(chai_types)

tea_shop = {
    "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    "tea": {"Green": "Mild","Black": "Strong"}
}

# print(tea_shop["chai"]["Ginger"])

squared_nums = {x: x*17 for x in range(1,11)}
# print(squared_nums)

keys = ["Masala","Ginger","Lemon"]
default_value = "Delicious"

new_dict = dict.fromkeys(keys,default_value)
# print(new_dict)


Teas = ["Masala","Ginger","Lemon"]
Taste = ["Spicy","Zesty","Mild"]

for key,value in zip(Teas,Taste):
    new_dict1 = {key: value}
    print(new_dict1)