'''
Script : test_unit
Author : Rijo Robert
Purpose : To unit test functions used in dhcp_log_analyser
Usage : python -m test_unit.py
'''
# Import modules
import unittest
import os
from Source.vendor import findvendor
from Source.csv_creator import create_csv_file
class TestDhcpLog(unittest.TestCase):
  
    def test_findvendor(self):
        get_mac_vendor_result = findvendor("a4:4c:c8")
        self.assertEqual(get_mac_vendor_result, "Dell Inc")

    def test_create_csv_file(self):
        OUTPUT_CSV_FILE = "example.csv"
        row_header = [('MAC ADDR', 'IP ADDR', 'HOSTNAME', 'VENDOR')]
        unique_to_csv_file_result = create_csv_file(OUTPUT_CSV_FILE, row_header)
        assert os.path.exists(OUTPUT_CSV_FILE) == True

if __name__ == '__main__':
    unittest.main()