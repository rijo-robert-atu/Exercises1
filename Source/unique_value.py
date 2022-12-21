"""
Script : unique_value
Author : Rijo Robert
Purpose : Filtering out the desired values from the dhcp log
Usage : python read_log.py      
"""
#Defining the variable for the function
seen = set()
new = []
#Defining a function for filter out the duplicate values
def unique_values(filter_list):
    #create a loop to pass the values
    for item in filter_list:
        #pass the values and write down the each line and check if any other line matching
        if item[0] not in seen:
            seen.add(item[0])
            new.append(item)
    #return the value to main        
    return new        
            