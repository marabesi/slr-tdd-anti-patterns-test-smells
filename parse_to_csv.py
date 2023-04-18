import json
import csv

from os import listdir

files = listdir("./results")

list_of_files = []
for file in files:
    with open("./results/{}".format(file), "r") as jsonFile:
        parsed = json.load(jsonFile)
        list_of_files.append(parsed)

data_file = open('parsed-google-scholar-to-csv.csv', 'w')
csv_writer = csv.writer(data_file)

count = 0
total = 0
for data in list_of_files:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())
    total += 1
 
data_file.close()

print("{} row(s)".format(total))
