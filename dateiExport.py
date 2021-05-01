import io


def toFile(fileName: str, byteStream: bytes) -> bytes:
    with io.open(fileName, 'wb') as fo:
        fo.write(byteStream)
