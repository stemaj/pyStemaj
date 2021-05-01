import unittest
import bytesExtractor
from byteStream import fromFile

class Test_bytesExtractor(unittest.TestCase):

    def test_cottbus(self):

        a = bytesExtractor.extractInnerPart(fromFile('./export/test.bin'), b'CO', b'BUS')
        self.assertTrue(isinstance(a, bytes))
        self.assertEqual(a, b'TT')
