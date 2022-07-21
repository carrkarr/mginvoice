import csv
import io

def read_csv(path):
    with io.open(path, 'rt', encoding='ISO-8859-1') as f:
        lines = f.read().split("\r\n")
    lines = [l.encode('ISO-8859-1').decode('ISO-8859-1') for l in lines]
    reader = csv.reader(lines, dialect=csv.excel)
    
    for row in reader:
        yield [x.encode('ascii').decode('ISO-8859-1') for x in row]

for row in read_csv("/temp/pasow/Reporte16-05-2022_excel_2007_sin nada.csv"):
    print(repr(row))
    
