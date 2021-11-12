import byteStream
import dateiExport
from six import ensure_str

def run(url, fileName):
    dateiExport.toFile(ensure_str(fileName), byteStream.fromUrl(ensure_str(url)))

#run("www.google.de", "resources/tests/goog.bin")