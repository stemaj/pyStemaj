import byteStream
import dateiExport

def run(url: str, fileName: str):
    dateiExport.toFile(fileName, byteStream.fromUrl(url))

#run("www.google.de", "resources/tests/goog.bin")