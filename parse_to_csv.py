import json
import csv
import pandas as pd

from os import listdir

file_path = "raw-result-from-google-scholar"
filename = "database/scholar.csv"

files = listdir("./" + file_path)
list_of_files = []

for file in files:
    with open("./{}/{}".format(file_path,file), "r") as jsonFile:
        parsed = json.load(jsonFile)
        list_of_files.append(parsed)

data_file = open('{}'.format(filename), 'w')
csv_writer = csv.writer(data_file)

count = 0
total = 0

for data in list_of_files:
    df = pd.json_normalize(data, sep='_')
    row = df.to_dict(orient='records')[0]
    row['id'] = total

    if count == 0:
        header = row.keys()
        csv_writer.writerow(header)
        count += 1

    csv_writer.writerow(row.values())
    total += 1
 
data_file.close()

print("{} row(s)".format(total))
