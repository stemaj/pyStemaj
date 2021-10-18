import unittest
import bytesExtractor
from byteStream import fromFile

class Test_bytesExtractor(unittest.TestCase):

    def test_cottbus(self):

        a = bytesExtractor.extractInnerPart(fromFile('./export/test.bin'), b'CO', b'BUS')
        self.assertTrue(isinstance(a, bytes))
        self.assertEqual(a, b'TT')

    def test_split(self):

        a = bytesExtractor.extractInnerPartAndSplit(b'Bla,und,Blubs,Test', b'Bla', b'Test', b',')
        self.assertTrue(isinstance(a, list))
        self.assertEqual(len(a), 2)
