import unittest
import subprocess
from flag import *
import base64
import time
import sys

cmd = 'python3'

class TestClients(unittest.TestCase):
    def test1(self):
        time.sleep(1)
        output = subprocess.check_output([cmd, '../client_1.py']).decode().strip()
        self.assertTrue(check_flag_validity(1, output))
    
    def test2(self):
        time.sleep(1)
        output = subprocess.check_output([cmd, '../client_2.py']).decode().strip().split()[1]
        self.assertTrue(check_flag_validity(2, output))
    
    def test3(self):
        time.sleep(1)
        output = subprocess.check_output([cmd, '../client_3.py']).decode().strip().split()
        self.assertEqual(output[0], 'random')
        self.assertEqual(output[1], 'port:')
        self.assertTrue(check_flag_validity(3, output[3]))

    def test4(self):
        time.sleep(1)
        output = subprocess.check_output([cmd, '../client_4.py']).decode().strip().split()
        self.assertEqual(len(output), 6)
        self.assertTrue(check_flag_validity(4, output[5]))

    def test5(self):
        time.sleep(1)
        output = subprocess.check_output([cmd, '../client_5.py']).decode().strip().split()
        self.assertEqual(len(output), 8)
        self.assertTrue(check_flag_validity(5, output[7]))

    def test6(self):
        time.sleep(1)
        output = subprocess.check_output([cmd, '../client_6.py']).decode().strip().split()
        self.assertEqual(len(output), 9)
        self.assertTrue(check_flag_validity(6, output[8]))

    def test7(self):
        time.sleep(1)
        output = subprocess.check_output([cmd, '../client_7.py']).decode().strip().split()
        self.assertEqual(len(output), 13)
        self.assertTrue(check_flag_validity(7, output[12]))

    def test8(self):
        time.sleep(1)
        output = subprocess.check_output([cmd, '../client_8.py']).decode().strip().split()
        self.assertEqual(len(output), 35)
        self.assertEqual(output[0].upper(), 'GET')
        self.assertEqual(output[1], '/')
        self.assertEqual(output[2].upper(), 'HTTP/1.0')
        self.assertTrue(check_flag_validity(8, output[33]))

    def test9(self):
        time.sleep(1)
        output = subprocess.check_output([cmd, '../client_9.py']).decode().strip().split()
        self.assertEqual(len(output), 25)
        self.assertEqual(output[0].upper(), 'POST')
        self.assertEqual(output[1], '/')
        self.assertEqual(output[2].upper(), 'HTTP/1.0')
        self.assertTrue(check_flag_validity(9, base64.b64decode(output[-1]).decode().strip()))

    def test10(self):
        time.sleep(1)
        output = subprocess.check_output([cmd, '../client_10.py']).decode().strip().split()
        self.assertEqual(len(output), 4)
        self.assertTrue(check_flag_validity(10, output[-1]))

if __name__ == '__main__':
    unittest.main()
    