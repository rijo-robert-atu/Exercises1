"""
Script : read_log
Author : Rijo Robert
Purpose : Filtering out the desired values from the dhcp log
Usage : python read_log.py      
"""
from Source.filter import dhcpack

myfinal = []

def read_log(logfilename):
    #open the logfile        
    logfile = open(logfilename, 'r')
    for myline in logfile:
    #the payload starts at position 34
        payload = myline[34:]
        #split the file with spaces
        list_of_values = payload.split(" ")
        #get the lines from the log starting with DHCPACK on
        if list_of_values[0] == "DHCPACK" and list_of_values[1] == "on":
            #pass the filtered list to dhcpack function
            final = dhcpack(list_of_values)
            #collect the return data from dhcpack function
            myfinal.append(final)
    #return the final value to main
    return myfinal
