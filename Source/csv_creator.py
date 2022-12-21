"""
Script : csv_creator
Author : Rijo Robert
Purpose : converting the final list to csv file
Usage : python csv_creator.py      
"""
import csv

def create_csv_file(filename,new):
    """To write csv file with the list provided"""
    #converting the list to csv using python built in functionality 
    with open(filename, 'w', encoding="utf-8") as outcsv:
        writer = csv.writer(outcsv, delimiter=',', quotechar='|',
        quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writerows([('IP', 'MAC', 'HOST', 'VENDOR')])
        writer.writerows(new)
    return None
