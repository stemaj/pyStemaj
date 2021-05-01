def extractInnerPart(content: bytes, beginString: bytes, endString: bytes) -> bytes:
    splitt = content.split(beginString)
    if len(splitt) > 1:
        splitt = splitt[1].split(endString)
        if len(splitt) > 1:
            return splitt[0]
    return b''