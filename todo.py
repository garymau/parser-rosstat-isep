import subprocess
import bs4
import sys


# todo: create xml file from doc
def make_xml(source_file_doc):
    if sys.platform == 'darwin':
        path_to_binary = "./bin/mac/antiword"
    else:
        raise Exception("This operating system is not supported")
    return subprocess.run([path_to_binary, "-m", "../UTF-8.txt",
                           "-x", "db", source_file_doc],
                          stdout=subprocess.PIPE, check=True).stdout


# todo: yield table with data
def yield_rows_from_xml(xml_string):
    soup = bs4.BeautifulSoup(xml_string, "xml")
    rows = soup.find_all('row')
    row_elements = []
    for row in rows:
        row_elements.clear()
        children = row.findChildren()
        for child in children:
            if child.name == 'entry':
                row_elements.append(child.text.strip().replace('\n', ''))
        yield row_elements[:]

source_file_doc = 'oper.doc'
xml_string = make_xml(source_file_doc)
with open('result.xml', mode='w+b') as xml_file:
    xml_file.write(xml_string)
gen = yield_rows_from_xml(xml_string)

# todo: must pass tests

# skipping top rows with column names
for i in range(4):
    _ = next(gen)

# check fourth row
row4 = next(gen)
assert row4[0] == "Валовой внутренний продукт, млрд.рублей"
assert row4[1] == "41782,11)"
    
# skip fifth row, it has omissions
_ = next(gen) 

# check sixth row
row6 = next(gen)
assert row6 == ["Продукция сельского хозяйства,  млрд.рублей",
                "712,6", "104,7", "149,1", "101,5", "105,7",
                "138,3", "104,7"]

# not todo:
# convert values like "41782,11)" to float(41782.1)
