from urllib3 import PoolManager
from shutil import copyfileobj
from six import ensure_str

def download(url, fileName):
    c = PoolManager()
    with c.request('GET', ensure_str(url), preload_content=False) as res, open(ensure_str(fileName), 'wb') as out_file:
        copyfileobj(res, out_file)
