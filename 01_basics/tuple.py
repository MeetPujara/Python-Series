#Tuple is Immutable
tea_types = ("Black","Green","Oolong")
more_tea = ("Herbal","Masala")

all_tea = more_tea + tea_types
# print(all_tea)

(BlackTea,GreenTea,OolongTea) = tea_types
print(tea_types)
print(BlackTea)