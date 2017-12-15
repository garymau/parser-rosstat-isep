"""

Intent is to download all doc files for ISEP publication into
   data/year/month/ folder
   
Url

    Root:
        http://www.gks.ru/bgd/free/B17_00/Main.htm
        
    Sample:    
        http://www.gks.ru/bgd/free/B17_00/IssWWW.exe/Stg/dk10/1-0.doc
       

"""

import arrow    
import requests
from pathlib import Path


def download(url, path):
    path = str(path)
    r = requests.get(url.strip(), stream=True)
    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            # filter out keep-alive new chunks
            if chunk:
                f.write(chunk)

def url(year: int, month: int, pub: str):
    last_digits = year-2000
    month = str(month).zfill(2)
    return ('http://www.gks.ru/bgd/free/' +             
            'B{}_00/'.format(last_digits) +            
            'IssWWW.exe/Stg/dk{}/'.format(month) + 
            '{}.doc'.format(pub))
    
assert url(2017, 10, '1-0') == ('http://www.gks.ru/bgd/free/B17_00/IssWWW.exe/'
                                'Stg/dk10/1-0.doc') 

class Folder:
    root = Path(__file__).parent
    
    def __init__(self, year: int, month: int):
        self.path = self.root / 'data' / str(year) / str(month) 
        if not self.path.exists():
            self.path.mkdir(parents=True)
            
class DocFile:        
    def __init__(self, year: int, month: int, pub: str):
        self.url = url(year, month, pub)
        self.path = Folder(year, month).path / f'{pub}.doc'

    def download(self):
        download(self.url, self.path)
        return self.path.stat().st_size
        
# TODO 1: change this list to actual file names
PARTS = ['1-0', '2-0', '3-0', '4-0', '5-0', '6-0', '7-0', '8-0']
    
def download_all(year, month):
     pass

def make_csv(year, month):
    pass

def extract(year, month):    
    pass 

def official_dates(): 
    start = arrow.get(2016, 1, 1)
    end = arrow.get(2017, 10, 1)
    for r in arrow.Arrow.range('month', start, end):
        yield r.year, r.month



if __name__ == "__main__":
    for y, m in official_dates():
        print(y, m)
        for postfix in PARTS:
            z = DocFile(2017, 10, postfix)
            print(z.download())
           
        #224256        
        #537 <--- no doc file 
        #537 <--- no doc file 
        #362496
        #488448
        #823808
        #413184
        #571904

# QUESTION: how far back in time can we run?
