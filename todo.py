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


def test_resulting_xml(xml_rows):
    # skipping top rows with column names
    for i in range(4):
        _ = next(xml_rows)

    # check fourth row
    row4 = next(xml_rows)
    assert row4[0] == "Валовой внутренний продукт, млрд.рублей"
    assert row4[1] == "41782,11)"

    # skip fifth row, it has omissions
    _ = next(xml_rows)

    # check sixth row
    row6 = next(xml_rows)
    assert row6 == ["Продукция сельского хозяйства,  млрд.рублей",
                    "712,6", "104,7", "149,1", "101,5", "105,7",
                    "138,3", "104,7"]

    # not todo:
    # convert values like "41782,11)" to float(41782.1)

source_file_doc = 'oper.doc'
# xml_string = make_xml(source_file_doc)
# with open('result.xml', mode='w+b') as xml_file:
#     xml_file.write(xml_string)
# xml_rows = yield_rows_from_xml(xml_string)
# test_resulting_xml(xml_rows)


def yield_rows_from_csv(path):
    import csv
    with open(path, newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
            yield row



# todo: must pass tests
def test_resulting_csv(csv_rows):

    for i in range(4):
        _ = next(csv_rows)

    # check fourth row
    row4 = next(csv_rows)
    assert row4[0] == "Валовой внутренний продукт, млрд.рублей"
    assert row4[1] == "41782,11)"

    # skip fifth row, it has omissions
    _ = next(csv_rows)

    # check sixth row
    row6 = next(csv_rows)
    assert row6 == ["Продукция сельского "
                    "хозяйства, млрд.рублей",
                    "712,6", "104,7", "149,1", "101,5", "105,7",
                    "138,3", "104,7"]

csv_rows = yield_rows_from_csv('oper.csv')
test_resulting_csv(csv_rows)

