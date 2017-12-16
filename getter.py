"""
Download doc files from publication and convert tables to CSV.
   
Publication root:
    http://www.gks.ru/bgd/free/B17_00/Main.htm
        
Sample url:    
    http://www.gks.ru/bgd/free/B17_00/IssWWW.exe/Stg/dk10/1-0.doc
"""

import arrow    
import requests
from pathlib import Path

from word import doc2csv, from_csv

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
    
    @staticmethod               
    def md(path):
        if not path.exists():
            path.mkdir(parents=True)
        return path    
               
    def __init__(self, year: int, month: int):
        self.path = self.root / 'data' / str(year) / str(month) 
    
    @property    
    def interim(self):
        return self.subfolder('interim')
    
    @property    
    def raw(self):
        return self.subfolder('raw')
        
    def subfolder(self, subfolder):
        return self.md(self.path / subfolder)
     
        
class DocFile:        
    def __init__(self, year: int, month: int, pub: str):
        self.year, self.month = year, month
        self.url = url(year, month, pub)
        self.path = Folder(year, month).raw / f'{pub}.doc'        

    @property
    def size(self):
        if self.path.exists():
            return int(round(self.path.stat().st_size / 1024, 0))

    def download(self):
        download(self.url, self.path)
        
    def to_csv(self, target):
        doc2csv(doc_path = self.path,
                csv_path = InterimCSV(self.year, self.month, target).path)                     
        

class InterimCSV:        
    def __init__(self, year: int, month: int, target: str):
        self.path = Folder(year, month).interim / f'{target}.csv'
    
    def from_csv(self):
        return from_csv(self.path)
        
class File:
    # TODO: continure dictionary based on 2017 10 (Октябрь)
    #       we want to use the dict to locate filenames based on keys like 'main' or 'ip'
    filesystem_a = dict(
         main=('1-0', 'Основные экономические и социальные показатели'),
         ip=('2-1-0', 'Индекс промышленного производства')
    )	
         #mng Добыча полезных ископаемых
         #mnf Обрабатывающие производства
         #pwr Обеспечение электрической энергией, газом и паром; кондиционирование воздуха
         #wat Водоснабжение; водоотведение, организация сбора и утилизации отходов, деятельность по ликвидации загрязнений
    	
         #agro   Сельское хозяйство
         #wood   Лесозаготовки
         #constr оительство
         #trans Транспорт
         
         #retail Розничная торговля
         #bop Внешняя торговля
    	
         #cpi Потребительские цены
         #ppi Цены производителей
    	
         #odue Просроченная кредиторская задолженность организаций
    	
         #soc Уровень жизни населения
    	
         #lab Занятость и безработица
    	
         #dem Демография     

    def __init__(self, year: int, month: int, target: str):
        self.target = target
        self.postfix = self.filesystem_a[target][0]
        self.doc = DocFile(year, month, self.postfix)
        self.csv = InterimCSV(year, month, self.target)
        
    def download(self):
        self.doc.download()
        
    def to_csv(self):
        self.doc.to_csv(self.target)

    def from_csv(self):
        return list(self.csv.from_csv())


# NOT TODO: filesystem_b based on 2017 09

PARTS = ['1-0', 
         '2-1', '2-1-0', '2-1-1', '2-1-2', '2-1-3', '2-1-4', 
         '2-2-0', '2-2-1', '2-2-2', '2-2-3', '2-2-4', 
         '2-3', '2-3-1', '2-3-2', 
         '2-4', '2-5', 
         '3-1', '3-2', 
         '4-0', '4-1', '4-2', 
         '5-0', '6-0', '7-0', '8-0']

    
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
    target = 'main' 
    #for y, m in official_dates():
    if True:
        y, m = 2017, 10 
        z = File(y, m, target)
        z.download()
        z.to_csv()
        print(y, m, target)
    
#    for y, m in official_dates():
#        print(y, m)
#        for postfix in PARTS:
#            z = DocFile(y, m, postfix)
#            z.download()
#            print(y, m, postfix, z.size)
           
# QUESTION: how far back in time can we run?

