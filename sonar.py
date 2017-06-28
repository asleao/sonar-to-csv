import json
import sys


def set_date(string):
    date_year = string[0:4]
    date_month = string[5:7]
    date_day = string[8:10]
    return date_day + '/' + date_month + '/' + date_year


def import_file(path):
    with open(path) as data_file:
        data = json.load(data_file)
    return data


def set_row(date, value):
    return date + ";" + value + ";\n"


json_data = import_file(sys.argv[1])['measures']
histories = json_data[0]['history']
csv_file = open(sys.argv[2], 'w')
header = 'date;value;\n'
csv_file.write(header)

for history in histories:
    date_hitory = history['date']
    date = set_date(history['date'])
    value = history['value']
    csv_file.write(set_row(date, value))

csv_file.close()
