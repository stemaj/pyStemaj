import unittest
import byteStream

class Test_holeByteStream(unittest.TestCase):

    fileName = './export/test.bin'

    def test_google(self):
        a = byteStream.fromUrl('www.google.de')
        self.assertTrue(isinstance(a, bytes))
        self.assertTrue(len(a) > 0)

    def test_unknownUrl(self):
        a = byteStream.fromUrl('www.huaiaucbucbuqwbch.de')
        self.assertTrue(isinstance(a, bytes))
        self.assertEqual(len(a),0)

    def test_importFile(self):
        a = byteStream.fromFile(self.fileName)
        self.assertTrue(isinstance(a, bytes))
        self.assertEqual(len(a),13)

