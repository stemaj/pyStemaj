#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import compile
from six import ensure_binary, ensure_str

#def extractInnerPart(content: bytes, beginString: str, endString: str) -> bytes:
def extractInnerPart(content, beginString, endString):
    """aus einem Bytehaufen den mittleren Teil extrahieren"""
    splitt = ensure_binary(content).split(ensure_binary(beginString))
    if len(splitt) > 1:
        splitt = splitt[1].split(ensure_binary(endString))
        if len(splitt) > 1:
            return ensure_binary(splitt[0])
    return ensure_binary('')

#def extractInnerPartAndSplit(content: bytes, beginString: str, endString: str, splitter: bytes):
def extractInnerPartAndSplit(content, beginString, endString, splitter):
    """aus einem Bytehaufen den mittleren Teil extrahieren und diesen mittels Trenner aufsplitten"""
    inner = extractInnerPart(content, beginString, endString)
    if len(inner) > 1:
        data = [bytes for bytes in inner.split(splitter) if bytes != b'']
        return data
    return b''

#def fromRegex(content: bytes, oneMatchPattern: bytes) -> bytes:
def fromRegex(content, oneMatchPattern):
    """gibt ein regex match als bytes zurück"""
    comp = compile(oneMatchPattern).findall(content)
    if len(comp) > 0:
        return comp[0]
    return b''
