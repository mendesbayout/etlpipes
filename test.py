import csv

with open('oferta_distribuicao.csv') as file_open:
    file_handle = csv.DictReader(file_open, fieldnames = "Nome_Emissor")

    for row in file_handle:
        print(row)