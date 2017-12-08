from os import getcwd

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


if __name__ == '__main__':
    
    
    # FIXME:
    # - must use word.to_csv()
    # - must be called outside this module    
    
    #def yield_continuous_rows_to_csv(input_doc, output_csv):
    #    # yield_continuous_rows_to_csv(input_doc=os.getcwd() + '\\' + 'oper.doc', output_csv='oper.csv')
    #    table_rows = list(yield_continious_rows(input_doc))
    #    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
    #        spamwriter = csv.writer(csvfile, delimiter=' ')
    #        for row in table_rows:
    #            spamwriter.writerow(row)

    # pseudocode: 
    # 1. locate doc file in the data/raw folder
    doc_file_path = ''
    # 2. get list of rows from csv
    gen = list(extract_rows(doc_file_path))
    # 3.  write generator to file 
    csv_file_path = ''
    save_to_csv = save_csv(csv_file_path, gen)
    # 4. test result
    test_result(gen)  
    
    
    #csv_rows = yield_rows_from_csv(getcwd() + '\\data\\processed\\' + 'oper.csv')
    #test_resulting_csv(csv_rows)
