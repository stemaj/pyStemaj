from urllib3 import PoolManager
from urllib3.exceptions import HTTPError
from io import open
from six import ensure_binary, ensure_str

def fromUrl(url):
    poolMgr = PoolManager(maxsize=10, cert_reqs='CERT_NONE')

    try:
        antwort = poolMgr.request('GET', ensure_str(url))
    except HTTPError:
        return ensure_binary('')

    if (antwort.status == 200):
        return ensure_binary(antwort.data)
    else:
        return ensure_binary('')


def fromFile(fileName):
    with open(ensure_str(fileName), 'rb') as fo:
        data = fo.read()
    return ensure_binary(data)
 