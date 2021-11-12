import os
import unittest
import sys
import six

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

import byteStream

class Test_holeByteStream(unittest.TestCase):

    fileName = os.path.join(root_folder, 'export/test.bin')

    def test_google(self):
        a = byteStream.fromUrl('www.google.de')
        self.assertTrue(isinstance(a, six.binary_type))
        self.assertTrue(len(a) > 0)

    def test_unknownUrl(self):
        a = byteStream.fromUrl('www.huaiaucbucbuqwbch.de')
        self.assertTrue(isinstance(a, six.binary_type))
        self.assertEqual(len(a),0)

    def test_importFile(self):
        a = byteStream.fromFile(self.fileName)
        self.assertTrue(isinstance(a, six.binary_type))
        self.assertEqual(len(a),13)

