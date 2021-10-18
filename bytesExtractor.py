def extractInnerPart(content: bytes, beginString: bytes, endString: bytes) -> bytes:
    """aus einem Bytehaufen den mittleren Teil extrahieren"""
    splitt = content.split(beginString)
    if len(splitt) > 1:
        splitt = splitt[1].split(endString)
        if len(splitt) > 1:
            return splitt[0]
    return b''

def extractInnerPartAndSplit(content: bytes, beginString: bytes, endString: bytes, splitter: bytes):
    """aus einem Bytehaufen den mittleren Teil extrahieren und diesen mittels Trenner aufsplitten"""
    inner = extractInnerPart(content, beginString, endString)
    if len(inner) > 1:
        data = [bytes for bytes in inner.split(splitter) if bytes != b'']
        print(data)
        return data
    return b''
