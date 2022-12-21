"""
Script : main
Author : Rijo Robert
Purpose : To analyse dhcp log and create a csv file with vendor details
Usage : python main.py    
    
"""
from Source.csv_creator import create_csv_file
from Source.unique_value import unique_values
from Source.read_log import read_log
#mention the filepath of the dhcp logfile
logfilename = "dhcpd.log"
#filter the dhcp log by ip,mac address,host
filter_list = read_log(logfilename)  
#Compare the filtered list with vendor list and get the vendor details
to_csv_list = unique_values(filter_list)
#convert the final list to csv format
create_csv_file('nodes.csv',to_csv_list)

