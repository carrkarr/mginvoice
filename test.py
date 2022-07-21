import chardet

with open('/temp/pasow/Reporte16-05-2022_excel_2007_sin nada.csv', 'rb') as f: 
    result = chardet.detect(f.read())

print (result['encoding'])
