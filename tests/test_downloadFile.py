import unittest
import downloadFile
from io import open
from os import remove
from os.path import exists

class Test_downloadFile(unittest.TestCase):

    mp3File = './export/test.mp3'

    @classmethod
    def setUpClass(self):
        if exists(self.mp3File):
            remove(self.mp3File)

    def test_anMp3(self):
        downloadFile.download("https://vgmsite.com/soundtracks/lotus-iii-amiga/tickgaqw/23_Game%20Over.mp3", self.mp3File)
        self.assertEqual(len(open(self.mp3File, 'rb').read()), 124175)
