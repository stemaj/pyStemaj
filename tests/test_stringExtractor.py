import os
import unittest
import sys
import six

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

import stringExtractor
from byteStream import fromFile

class Test_stringExtractor(unittest.TestCase):

    fileName = os.path.join(root_folder,'export/test.bin')

    def test_cottbus(self):
        a = stringExtractor.matchByRegex(fromFile(self.fileName), six.b('COTT(.+)\\x00'))
        self.assertTrue(isinstance(a, six.string_types))
        self.assertEqual(a, 'BUS')
