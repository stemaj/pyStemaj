import unittest
import stringExtractor
from byteStream import fromFile

class Test_stringExtractor(unittest.TestCase):

    def test_cottbus(self):
        a = stringExtractor.matchByRegex(fromFile('./export/test.bin'), b'COTT(.+)\\x00')
        self.assertTrue(isinstance(a, str))
        self.assertEqual(a, 'BUS')
