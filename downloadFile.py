import urllib3, shutil

def download(url: str, fileName: str) -> None:
    c = urllib3.PoolManager()
    with c.request('GET', url, preload_content=False) as res, open(fileName, 'wb') as out_file:
        shutil.copyfileobj(res, out_file)
