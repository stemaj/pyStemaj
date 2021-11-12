import os
import unittest
import sys
import six

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

import bytesExtractor
from byteStream import fromFile

class Test_bytesExtractor(unittest.TestCase):

    fileName = os.path.join(root_folder, 'export/test.bin')

    def test_cottbus(self):

        a = bytesExtractor.extractInnerPart(fromFile(self.fileName), six.b('CO'), six.b('BUS'))
        self.assertTrue(isinstance(a, bytes))
        self.assertEqual(a, b'TT')

    def test_split(self):

        a = bytesExtractor.extractInnerPartAndSplit(b'Bla,und,Blubs,Test', b'Bla', b'Test', b',')
        self.assertTrue(isinstance(a, list))
        self.assertEqual(len(a), 2)

    def test_regex(self):

        a = bytesExtractor.fromRegex(fromFile(self.fileName), b'\x00\x01\x02CO(.+)BUS\x00\x01\x02')
        self.assertTrue(isinstance(a, bytes))
        self.assertEqual(a, b'TT')

