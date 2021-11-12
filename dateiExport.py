import io
from six import ensure_str, ensure_binary

#def toFile(fileName: str, byteStream: bytes) -> bytes:
def toFile(fileName, byteStream):
    with io.open(ensure_str(fileName), 'wb') as fo:
        fo.write(ensure_binary(byteStream))
