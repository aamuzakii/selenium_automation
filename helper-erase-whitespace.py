def erase_space(): 
    raw_str = "Acc  - defdf  ()dcdc.xls"
    str_to_list = raw_str.split(' ')
    print(str_to_list)

    new_list = []
    def erase_space(variable): 
        if variable != '': 
            return True
        else: 
            return False

    filtered = filter(erase_space, str_to_list) 

    for s in filtered: 
        new_list.append(s)

    str1 = ""      
    for ele in new_list:  
        str1 += ele  
    print(str1)
    return str1     
        
erase_space()
