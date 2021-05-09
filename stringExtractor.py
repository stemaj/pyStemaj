from re import search

def matchByRegex(daten: bytes, pattern: bytes) -> str:
    match = search(pattern, daten)
    if match is not None and len(match.groups()) > 0:
        return match.group(1).decode('utf-8')

def matchesByRegex2(daten: bytes, pattern: bytes) -> str:
    match = search(pattern, daten)
    if match is not None and len(match.groups()) > 0:
        return [match.group(1).decode('utf-8'), match.group(2).decode('utf-8')]

