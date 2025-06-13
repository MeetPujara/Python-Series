def pairs(**names):
    # result = []
    # for key, value in names.items():
    #     result.append((key, value))  
    # return result
    
    #The Above 4line returns list of tuples
    return names #This Returns Dictionary
    
name_dict={}
while True:
    input_str_key = input("Enter Key: ")
    input_str_value = input("Enter Value: ")

    if (input_str_key or input_str_value) == "":
        break
    else:
        name_dict[input_str_key] = input_str_value 
        
print("The Name List Are: ",pairs(**name_dict))
            