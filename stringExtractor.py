from re import search
from six import ensure_str

#def matchByRegex(daten: bytes, pattern: bytes) -> str:
def matchByRegex(daten, pattern):
    match = search(pattern, daten)
    if match is not None and len(match.groups()) > 0:
        return ensure_str(match.group(1))

#def matchesByRegex2(daten: bytes, pattern: bytes):
def matchesByRegex2(daten, pattern):
    match = search(pattern, daten)
    if match is not None and len(match.groups()) > 0:
        return [ensure_str(match.group(1)), ensure_str(match.group(2))]

#def matchesByRegex3(daten: bytes, pattern: bytes):
def matchesByRegex3(daten, pattern):
    match = search(pattern, daten)
    if match is not None and len(match.groups()) > 0:
        return [ensure_str(match.group(1)), ensure_str(match.group(2)), ensure_str(match.group(3))]
