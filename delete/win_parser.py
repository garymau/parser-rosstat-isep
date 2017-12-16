from helper import DataFolder
from word import yield_continious_rows, to_csv, from_csv

def doc2csv(doc_filepath,  csv_filepath):
   # get list of rows from csv
   gen = yield_continious_rows(doc_filepath)
   #write generator to file 
   to_csv(gen, csv_filepath)
    
expected_rows = [
 ['Валовой внутренний продукт, млрд.рублей',
  '41782,11)',
  '101,52)',
  '',
  '',
  '99,53)',
  '',
  ''],
 ['Индекс промышленного производства4)',
  '',
  '101,5',
  '102,0',
  '101,9',
  '101,5',
  '101,5',
  '101,3'],
 ['Продукция сельского хозяйства, млрд.рублей',
  '712,6',
  '104,7',
  '149,1',
  '101,5',
  '105,7',
  '138,3',
  '104,7']
 ]

if __name__ == '__main__':
    doc_filepath = str(DataFolder.raw / 'oper.doc')
    csv_filepath = str(DataFolder.interim / 'oper.csv')
    doc2csv(doc_filepath,  csv_filepath)    
    gen = list(from_csv(csv_filepath))    
    # check
    assert gen[4] == expected_rows[0]
    # TODO: extract dictionaries
