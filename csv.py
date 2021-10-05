import csv

class Csv_Tool:
    _target = None
    _reader = None
    _writer = None

    def __init__(self, target, mode):
        if mode == 'r':
            _reader = csv.reader(target)
        if mode == 'w':
            _writer = csv.writer(target)

    def get_reader():
        return _reader

    def read_row():
        for row in _reader:
            return row

    def read_all():
        ret = [ row for row in _reader ]
        return ret

    def read_row_by_key(key):
        rows = read_all()
        for row in rows:
            if row[0] == key:
                return row
        return None

    def read_column_by_key(key):
        index = None
        rows = read_all()
        for i, element in enumerate(rows[0]):
            if element == key:
                index = i
                break
        if !index:
            return None

        column = []
        for row in rows:
            column.append(row[index])
        return column

    def get_writer():
        return _writer

    def write_row(row):
        _writer.writerow(row)

    def write_all(rows):
        _writer.writerows(rows)

    def convert_row_to_column(rows):
        ret = []
        for i in len(rows[0]):
            tmp = []
            for row in rows:
                tmp.append(row[i])
            ret.append(tmp)
        return ret
