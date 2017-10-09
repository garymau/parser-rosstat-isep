Data source
===========

First table page in ISEP publication. 

Publication home: 
	<http://www.gks.ru/wps/wcm/connect/rosstat_main/rosstat/ru/statistics/publications/catalog/doc_1140087276688>
	
Local files for one month:
	- [oper.doc](oper.doc) (one table in file)
	- [oper.pdf](oper.pdf) (table at page 4)
	
Pseudocode
==========

1. download files from web based on (year, month)
2. convert word or pdf to something readable (csv/xml)
3. based on further row/column specification, extract key datapoints form table 
4. emit key data as  ```variable_name-frequency-date-value``` dictionaries
5. same result as json

Platform
========

Best case: the solution works on Windows and Linux.
Second best: there two solutions, one on Windows works the same as on Linux. 

  
Output
======
	
From table:	
	- must emit cells by row 
  - emit name-frequency-date-value dictionaries
	
	
Some approaches
===============

Parse pdf
---------

- ```pip install pdfminer.six```
- ```python D:\Continuum\Anaconda3\Scripts\pdf2txt.py -p 4 oper.pdf -t xml > oper.xml```
- parse oper.xml next

Parse word
----------

- may use <https://github.com/mini-kep/parser-rosstat-kep/tree/master/src/word2csv>

References
==========

Tech stack for parsing word at <https://gist.github.com/epogrebnyak/252e5b568d58b7e9c635c2723d81c850>

