import unittest
from byteStream import getExampleStream

class Test_holeByteStream(unittest.TestCase):

    def test_one(self):
        a = getExampleStream()
        self.assertFalse(isinstance(a, str))
        self.assertTrue(isinstance(a, bytes))
        self.assertNotEqual(a, 'Bla')
        self.assertEqual(a, b'Bla')
