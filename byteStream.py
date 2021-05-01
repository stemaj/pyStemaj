from urllib3 import PoolManager
from urllib3.exceptions import HTTPError
from io import open


def fromUrl(url: str) -> bytes:
    poolMgr = PoolManager(maxsize=10, cert_reqs='CERT_NONE')

    try:
        antwort = poolMgr.request('GET', url)
    except HTTPError:
        return b''

    if (antwort.status == 200):
        return antwort.data
    else:
        return b''


def fromFile(fileName: str) -> bytes:
    with open(fileName, 'rb') as fo:
        data = fo.read()
    return data
