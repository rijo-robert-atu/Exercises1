"""
Script : filter
Author : Rijo Robert
Purpose : filterng out the values to ip,mac,host,vendor
Usage : python filter.py      
"""
from Source.vendor import findvendor

def dhcpack(list_of_values): 
    #defining the variables
    ipv4 = []
    mac =[]
    node = []
    host_list = []
    oui_mac = []   
    #getting the 2nd postion values from list
    ipv4.append(list_of_values[2])
    #getting the 4th postion values from list
    mac.append(list_of_values[4])
    #Call the findvendor module and list out the vendor
    oui_mac.append(findvendor(list_of_values[4]))
    #getting the 5th postion values from list and remove ()
    node=list_of_values[5].strip('(').strip(')')
    #change the values via with no_host
    if node == "via":
        host="no_host"
        host_list.append(host)
    else :
        host_list.append(node)  
    #combine all the values 
    final_list = ipv4+ mac+ host_list+ oui_mac
    #return the values to the main
    return final_list
    
