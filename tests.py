import unittest
import subprocess
from flag import *
import base64

class TestClients(unittest.TestCase):
    def test1(self):
        output = subprocess.check_output(['python', '../client_1.py']).decode().strip()
        self.assertTrue(check_flag_validity(1, output))
    
    def test2(self):
        output = subprocess.check_output(['python', '../client_2.py']).decode().strip()
        self.assertTrue(check_flag_validity(2, output))
    
    def test3(self):
        output = subprocess.check_output(['python', '../client_3.py']).decode().strip().split()
        self.assertEqual(output[0], 'random')
        self.assertEqual(output[1], 'port:')
        self.assertTrue(check_flag_validity(3, output[3]))

    def test4(self):
        output = subprocess.check_output(['python', '../client_4.py']).decode().strip().split()
        self.assertEqual(len(output), 6)
        self.assertTrue(check_flag_validity(4, output[5]))

    def test5(self):
        output = subprocess.check_output(['python', '../client_5.py']).decode().strip().split()
        self.assertEqual(len(output), 8)
        self.assertTrue(check_flag_validity(5, output[7]))

    def test6(self):
        output = subprocess.check_output(['python', '../client_6.py']).decode().strip().split()
        self.assertEqual(len(output), 9)
        self.assertTrue(check_flag_validity(6, output[8]))

    def test7(self):
        output = subprocess.check_output(['python', '../client_7.py']).decode().strip().split()
        self.assertEqual(len(output), 13)
        self.assertTrue(check_flag_validity(7, output[12]))

    def test8(self):
        output = subprocess.check_output(['python', '../client_8.py']).decode().strip().split()
        self.assertEqual(len(output), 35)
        self.assertEqual(output[0].upper(), 'GET')
        self.assertEqual(output[1], '/')
        self.assertEqual(output[2].upper(), 'HTTP/1.0')
        self.assertTrue(check_flag_validity(8, output[33]))

    def test9(self):
        output = subprocess.check_output(['python', '../client_9.py']).decode().strip().split()
        self.assertEqual(len(output), 25)
        self.assertEqual(output[0].upper(), 'POST')
        self.assertEqual(output[1], '/')
        self.assertEqual(output[2].upper(), 'HTTP/1.0')
        self.assertTrue(check_flag_validity(9, base64.b64decode(output[-1]).decode().strip()))

    def test10(self):
        output = subprocess.check_output(['python', '../client_10.py']).decode().strip().split()
        self.assertEqual(len(output), 4)
        self.assertTrue(check_flag_validity(10, output[-1]))

if __name__ == '__main__':
    unittest.main()
    