from re import search

def matchByRegex(daten: bytes, pattern: bytes) -> str:
    match = search(pattern, daten)
    if match is not None and len(match.groups()) > 0:
        return match.group(1).decode('utf-8')
