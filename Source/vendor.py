"""
Script : vendor
Author : Rijo Robert
Purpose : comparing the mac address and list out the vendor
Usage : python vendor.py      
"""
#creating the dictionary for comparing mac values
vendor_dic = {'c8:4b:d6' : 'Dell Inc',
          '18:68:cb' : 'Hangzhou',
          'b8:27:eb' : 'Raspberry',
          'c0:25:a5' : 'Dell Inc',
          'a4:4c:c8' : 'Dell Inc',
          'bc:5f:f4' : 'ASRock'
          }
# function to comare the values
def findvendor(oui):
    #spliting the values till the 8th position
    oui_cutting=oui[0:8] 
    result=vendor_dic[oui_cutting]
    #return the value to filter module
    return result
#this module can be used as a standalone script
if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
    input_mac = input("enter mac address:")
    print("Vendor is:", findvendor(input_mac))
    