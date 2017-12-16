from getter import File

year, month = 2017, 10

COLUMNS_DEFAULT = {1:'bln_rub', 2:'yoy', 3:'rog'}

d1 = dict(
    substring = 'Индекс промышленного производства',
    name = 'INDPRO'
)

d2 = dict(
    substring = 'Индекс промышленного производства',
    column = 3,
    name = 'INDPRO'
)


rows = File(year, month, 'main').from_csv()

def mapper(year, month, d):
    pass

assert mapper(year, month, d1) == [
    {'name': 'INDPRO_yoy', 'date': '2017-10', 'value': 100.0},         
    {'name': 'INDPRO_rog', 'date': '2017-10', 'value': 105.7},         
]