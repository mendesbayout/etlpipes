import csv
import json

# file configuration


fieldnames = ("CNPJ_FUNDO", "CNPJ_FUNDO", "DENOM_SOCIAL", "DT_COMPTC")

# encodings = ['utf-8', 'windows-1250', 'windows-1252'] # add more
# for e in encodings:
# try:
# fh = codecs.open('perfil_mensal_fi_202101.csv', 'r', encoding = e)
# fh.readlines()
# fh.seek(0)
# except UnicodeDecodeError:
# print('got unicode error with %s , trying different encoding' % e)
# else:
# print('opening the file with encoding:  %s ' % e)
# break

# Read and transform csvIDENTIFY E#
csv_file = 'eventual_fi_2016.csv'
json_file = 'eventual_fi_2016.json'



def read_CSV(csv_file, json_file):
    csv_rows = []
    with open(csv_file, encoding = 'windows-1252') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames = fieldnames, delimiter = ';')
        field = reader.fieldnames

        # iterating through csv fields(input)
        for row in reader:
            csv_rows.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        convert_write_json(csv_rows, json_file)


# Convert csv data into json
def convert_write_json(data, json_file):
    with open(json_file, "w", encoding = 'utf-8') as file:
        file.write(json.dumps(data, indent = 4, separators = (',', ': '), ensure_ascii=False))
        file.write(json.dumps(data, ensure_ascii=False))

        #print("data loading..")
        #print(data)



read_CSV(csv_file, json_file)

with open('perfil_mensal_fi_202101.csv') as f:
    print(f)

with open('perfil_mensal_fi_202101.json') as f:
    print(f)
