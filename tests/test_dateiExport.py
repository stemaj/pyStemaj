import os
import unittest
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

import dateiExport
from io import open
from os import remove
from os.path import exists


class Test_dateiExport(unittest.TestCase):

    fileName = os.path.join(root_folder,'export/test.bin')

    @classmethod
    def setUpClass(self):
        if exists(self.fileName):
            remove(self.fileName)

    def test_exportSomeBytes(self):
        ba = bytes(bytearray([0, 1, 2, ord('C'), ord('O'), ord('T'), ord('T'), ord('B'), ord('U'), ord('S'), 0, 1, 2]))
        dateiExport.toFile(self.fileName, ba)
        self.assertEqual(len(open(self.fileName, 'rb').read()), 13)
