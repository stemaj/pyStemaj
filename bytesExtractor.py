from re import compile

def extractInnerPart(content: bytes, beginString: str, endString: str) -> bytes:
    """aus einem Bytehaufen den mittleren Teil extrahieren"""
    splitt = content.split(beginString)
    if len(splitt) > 1:
        splitt = splitt[1].split(endString)
        if len(splitt) > 1:
            return splitt[0]
    return b''

def extractInnerPartAndSplit(content: bytes, beginString: str, endString: str, splitter: bytes):
    """aus einem Bytehaufen den mittleren Teil extrahieren und diesen mittels Trenner aufsplitten"""
    inner = extractInnerPart(content, beginString, endString)
    if len(inner) > 1:
        data = [bytes for bytes in inner.split(splitter) if bytes != b'']
        print(data)
        return data
    return b''

def fromRegex(content: bytes, oneMatchPattern: bytes) -> bytes:
    """gibt ein regex match als bytes zurück"""
    comp = compile(oneMatchPattern).findall(content)
    if len(comp) > 0:
        return comp[0]
    return b''
