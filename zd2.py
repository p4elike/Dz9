import requests
from pprint import pprint
import pathlib
from pathlib import Path

def get_url():
    url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    p = {"path": path, "overwrite": "true", "fields": "Link"}
    h = {'Content-Type': 'application/json',
         'Authorization': token
         }
    response = requests.get(url=url,  headers=h, params=p)
    r1 = response.json()
    pprint(r1)
    r2 = r1.get('href')
    pprint(r2)
    return r2


def file_of_disk():
    url = get_url()
    h = {'Content-Type': 'application/json',
         'Authorization': token
         }
    p = {"path": path, "overwrite": "true"}
    response = requests.put(url=url,  headers=h, params=p)
    pprint(response.status_code)

if __name__ == '__main__':
    path = Path("Games", "некий_файл.txt")
    token = '...'
    upload = file_of_disk()
    get_url()
