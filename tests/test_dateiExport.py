import unittest
import dateiExport
from io import open
from os import remove
from os.path import exists


class Test_dateiExport(unittest.TestCase):

    fileName = './export/test.bin'

    @classmethod
    def setUpClass(self):
        if exists(self.fileName):
            remove(self.fileName)

    def test_exportSomeBytes(self):
        ba = bytes([0, 1, 2, ord('C'), ord('O'), ord('T'), ord('T'), ord('B'), ord('U'), ord('S'), 0, 1, 2])
        dateiExport.toFile(self.fileName, ba)
        self.assertEqual(len(open(self.fileName, 'rb').read()), 13)
