Use case
========

We need to do the fllowing:
1. download a publication as Word or PDF file from Rossat web site
2. parse the table in Section 1 (```"ОСНОВНЫЕ ЭКОНОМИЧЕСКИЕ И СОЦИАЛЬНЫЕ ПОКАЗАТЕЛИ"```) preserving 
cell table structure 
3. return several cell values as dictionaries with assigned variable name, date, frequency and value

#### Example: 


Август 2017г. | В % к августу 2016 г. | В % к июлю 2017 г. |
--------------|-----------------------|--------------------|
Валовой внутренний продукт, млрд.рублей | 41782,11) | 101,52) |       |
Индекс промышленного производства4)     |           | 101,5   | 102,0 |
Продукция сельского хозяйства, млрд.рублей | 712,6  | 104,7   | 149,1 |

Lines 1 - we still need this data, but they are for different dates and not a monthly frequency,
must be treated as a special case. 

Lines 2 and 3 should read as:

```python 
[
    dict(name='INDPRO_yoy', freq='m', date='2017-08', value=101.5),
    dict(name='INDPRO_rog', freq='m', date='2017-08', value=102.0), 
    dict(name='AGROPROD_bln_rub', freq='m', date='2017-08', value=712.6),
    dict(name='AGROPROD_yoy', freq='m', date='2017-08', value=104.7),
    dict(name='AGROPROD_rog', freq='m', date='2017-08', value=149.1)
    ]
```

Table structure
===============

#### Columns

1. First three data columns contain information of interest:
- `"Август 2017г."` - this is publication month, August, returns absolute values
- `в % к августу 2016 г.` - this is 'yoy' (year on year) rate of growth
- `в % к июлю 2016 г.` - this is 'rog' (rate of growth) change

2. We disregard the rest of data columns


#### Rows

Several rows contain data for different months other than August.

1. Previous period from year start:
- `Валовой внутренний продукт, млрд.рублей`
- `Инвестиции в основной капитал, млрд.рублей` 

2. One month behind:
- `Внешнеторговый оборот, млрд.долларов США` and 2 subsequent lines


Links
=====

Publication home: 
    <http://www.gks.ru/wps/wcm/connect/rosstat_main/rosstat/ru/statistics/publications/catalog/doc_1140087276688>
	
Local files for one month:

  - [oper.doc](oper.doc) (one table in file)
  - [oper.pdf](oper.pdf) (table at page 4)
	
Pseudocode
==========

1. download files from web based on (year, month)
2. convert word or pdf to something readable (csv/xml)
3. extract cells form table 
4. emit data as  ```variable_name-frequency-date-value``` dictionaries


Platform
========

Best case: the solution works on Windows and Linux.

Second best: there two solutions, one on Windows and other one for Linux. 


Some approaches
===============

A. Parse pdf
------------

- ```pip install pdfminer.six```
- ```python D:\Continuum\Anaconda3\Scripts\pdf2txt.py -p 4 oper.pdf -t xml > oper.xml```
- parse oper.xml next

В. Parse word
-------------

- on Windows may use <https://github.com/mini-kep/parser-rosstat-kep/tree/master/src/word2csv>

- tech stack for parsing word at <https://gist.github.com/epogrebnyak/252e5b568d58b7e9c635c2723d81c850>
