import unittest
import subprocess
from flag import *
import base64
import time
import sys

cmd = 'python3'

class TestClients(unittest.TestCase):
    units = ["bits", "kibit", "kbit", "mibit", "mbit", "gibit", "gbit", "kbps", "mbps", "gbps", "kb", "mb", "gb"]
    
    def test1(self):
        time.sleep(2)
        output = subprocess.check_output([cmd, '../client_1.py']).decode().strip()
        self.assertTrue(check_flag_validity(1, output))
    
    def test2(self):
        time.sleep(2)
        output = subprocess.check_output([cmd, '../client_2.py']).decode().strip().split()
        self.assertEqual(output[0].upper(), 'HELO')
        self.assertTrue(check_flag_validity(2, output[1]))
    
    def test3(self):
        time.sleep(2)
        output = subprocess.check_output([cmd, '../client_3.py']).decode().strip().split()
        self.assertEqual(output[0], 'random')
        self.assertEqual(output[1], 'port:')
        self.assertEqual(type( int(output[2]) ), int)
        self.assertTrue(check_flag_validity(3, output[3]))

    def test4(self):
        time.sleep(2)
        output = subprocess.check_output([cmd, '../client_4.py']).decode().strip().split()
        self.assertEqual(type( int(output[0]) ), int)
        assert(output[1].lower() in self.units )
        self.assertEqual(type( int(output[2]) ), int)
        assert(output[3].lower() in self.units )
        self.assertEqual(type( float(output[4]) ), float)
        self.assertEqual(len(output), 6)
        self.assertTrue(check_flag_validity(4, output[5]))

    def test5(self):
        time.sleep(2)
        output = subprocess.check_output([cmd, '../client_5.py']).decode().strip().split()
        self.assertEqual(len(output), 8)
        l = output[0].split('=')
        self.assertEqual(l[0], 'L')
        self.assertEqual(type(int(l[1])), int)
        assert(output[1].lower() in self.units)
        r1 = output[2].split('=')
        self.assertEqual(r1[0], 'R1')
        self.assertEqual(type(int(r1[1])), int)
        assert(output[3].lower() in self.units)
        r2 = output[4].split('=')
        self.assertEqual(r2[0], 'R2')
        self.assertEqual(type(int(r2[1])), int)
        assert(output[5].lower() in self.units)
        self.assertEqual(type( float(output[6]) ), float)
        self.assertTrue(check_flag_validity(5, output[7]))

    def test6(self):
        time.sleep(2)
        output = subprocess.check_output([cmd, '../client_6.py']).decode().strip().split()
        self.assertEqual(len(output), 9)
        self.assertEqual(output[0].lower(), 'syn')
        self.assertEqual(output[1].lower(), 'seq=0')
        self.assertEqual(output[2].lower(), 'syn,ack')
        self.assertEqual(output[3].lower(), 'seq=0')
        self.assertEqual(output[4].lower(), 'ack=1')
        self.assertEqual(output[5].lower(), 'ack')
        self.assertEqual(output[6].lower(), 'seq=1')
        self.assertEqual(output[7].lower(), 'ack=1')
        self.assertTrue(check_flag_validity(6, output[8]))

    def test7(self):
        time.sleep(2)
        output = subprocess.check_output([cmd, '../client_7.py']).decode().strip().split()
        self.assertEqual(len(output), 13)
        self.assertEqual(output[0].lower(), 'fin,ack')
        self.checkSeqAck( output[1], 'seq' )
        self.checkSeqAck( output[2], 'ack' )
        self.checkSeqAck( output[4], 'seq' )
        self.checkSeqAck( output[5], 'ack' )
        self.assertEqual(output[6].lower(), 'fin,ack')
        self.checkSeqAck( output[7], 'seq' )
        self.checkSeqAck( output[8], 'ack' )
        self.assertEqual(output[9].lower(), 'ack')
        self.checkSeqAck( output[10], 'seq' )
        self.checkSeqAck( output[11], 'ack' )
        self.assertTrue(check_flag_validity(7, output[12]))

    def checkSeqAck( self, value, string ):
        tmp = value.lower().split('=')
        self.assertEqual(tmp[0], string)
        self.assertEqual(type(int(tmp[1])), int)

    def test8(self):
        time.sleep(2)
        output = subprocess.check_output([cmd, '../client_8.py']).decode().strip().lower()
        if('host:10.40.0.46' in output):
            output = output.replace('host:10.40.0.46', 'host: 10.40.0.46')
        output = output.split()
        self.assertEqual(len(output), 36)
        self.assertEqual(output[0], 'get')
        self.assertEqual(output[1], '/')
        self.assertEqual(output[2], 'http/1.0')
        self.assertEqual(output[3], 'host:')
        self.assertIn(output[4], ['10.40.0.46', '10.40.0.46:9997'])
        self.assertEqual(output[5], 'http/1.0')
        self.assertEqual(output[6], '200')
        self.assertEqual(output[7], 'ok')
        self.assertEqual(output[8], 'server:')
        self.assertEqual(output[9], 'simplehttp/0.6')
        self.assertEqual(type(output[10]), str)
        self.assertEqual(output[11], 'date:')
        self.assertIn(output[12][:3], ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'])
        self.assertEqual(type(int(output[13])), int)
        self.assertIn(output[14], ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
        self.assertGreaterEqual(int(output[15]), 2021)
        self.assertEqual(len(output[16]), 8)
        tmp = output[16].split(':')
        self.assertEqual(type(int(tmp[0])), int)
        self.assertEqual(type(int(tmp[1])), int)
        self.assertEqual(type(int(tmp[2])), int)
        self.assertEqual(output[17], 'gmt')
        self.assertEqual(output[18], 'content-type:')
        self.assertEqual(output[19], 'text/html')
        self.assertEqual(output[20], 'content-length:')
        self.assertEqual(type(int(output[21])), int)
        self.assertEqual(output[22], 'last-modified:')
        self.assertIn(output[23][:3], ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'])
        self.assertEqual(type(int(output[24])), int)
        self.assertIn(output[25], ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
        self.assertGreaterEqual(int(output[26]), 2021)
        self.assertEqual(len(output[27]), 8)
        tmp = output[27].split(':')
        self.assertEqual(type(int(tmp[0])), int)
        self.assertEqual(type(int(tmp[1])), int)
        self.assertEqual(type(int(tmp[2])), int)
        self.assertEqual(output[28], 'gmt')
        self.assertEqual(output[29], "it's")
        self.assertEqual(output[30], 'not')
        self.assertEqual(output[31], 'that')
        self.assertEqual(output[32], 'easy')
        self.assertEqual(output[33], '<!--')
        self.assertTrue(check_flag_validity(8, output[34]))
        self.assertEqual(output[35], '-->')

    def test9(self):
        time.sleep(2)
        output = subprocess.check_output([cmd, '../client_9.py']).decode().strip()
        if('host:10.40.0.46' in output.lower()):
            output = output.lower().replace('host:10.40.0.46', 'host: 10.40.0.46')
        output = output.split()

        self.assertEqual(len(output), 25)
        self.assertEqual(output[0].lower(), 'post')
        self.assertEqual(output[1], '/')
        self.assertEqual(output[2].lower(), 'http/1.0')
        self.assertEqual(output[3].lower(), 'host:')
        self.assertIn(output[4].lower(), ['10.40.0.46', '10.40.0.46:9998'])
        self.assertEqual(output[5].lower(), 'content-type:')
        self.assertEqual(output[6].lower(), 'application/text')
        self.assertEqual(output[7].lower(), 'content-length:')
        self.assertEqual(type(int(output[8])), int)
        self.assertEqual(output[9].lower(), 'http/1.0')
        self.assertEqual(output[10].lower(), '200')
        self.assertEqual(output[11].lower(), 'ok')
        self.assertEqual(output[12].lower(), 'server:')
        self.assertEqual(output[13].lower(), 'basehttp/0.6')
        self.assertEqual(type(output[14]), str)
        self.assertEqual(output[15].lower(), 'date:')
        self.assertIn(output[16].lower()[:3], ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'])
        self.assertEqual(type(int(output[17])), int)
        self.assertIn(output[18].lower(), ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
        self.assertGreaterEqual(int(output[19]), 2021)
        self.assertEqual(len(output[20].lower()), 8)
        tmp = output[20].lower().split(':')
        self.assertEqual(type(int(tmp[0])), int)
        self.assertEqual(type(int(tmp[1])), int)
        self.assertEqual(type(int(tmp[2])), int)
        self.assertEqual(output[21].lower(), 'gmt')
        self.assertEqual(output[22].lower(), 'base64')
        self.assertEqual(output[23].lower(), 'response:')
        self.assertEqual(len( output[-1] ), 88)
        self.assertTrue(check_flag_validity(9, base64.b64decode(output[-1]).decode().strip()))

    def test10(self):
        time.sleep(2)
        output = subprocess.check_output([cmd, '../client_10.py']).decode().strip()
        self.assertNotIn("Wrong answer", output)
        output = output.split()
        self.assertEqual(len(output), 4)
        self.assertEqual(len(output[0]), 8)
        self.assertEqual(len(output[1]), 8)
        self.assertEqual(len(output[2]), 8)
        for i in [0,1,2]:
            self.assertTrue( self.checkBinaryString( output[i]) )
        self.assertTrue(check_flag_validity(10, output[-1]))

    def checkBinaryString(self, string):
        for s in string:
            if( int(s) > 1 or int(s) < 0 ): return False
        return True

if __name__ == '__main__':
    unittest.main()
    