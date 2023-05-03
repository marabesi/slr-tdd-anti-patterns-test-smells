import json
import csv
import pandas as pd

from os import listdir

file_path = "raw-result-from-google-scholar"
filename = "database/scholar.csv"

files = listdir("./" + file_path)
list_of_files = []

default_schema = dict({
  "id": "KO",
  "container_type": "KO",
  "source": "KO",
  "bib": {
    "title": "KO",
    "author": "KO",
    "pub_year": "KO",
    "venue": "KO",
    "abstract": "KO"
  },
  "filled": "KO",
  "gsrank": "KO",
  "pub_url": "KO",
  "author_id": "KO",
  "url_scholarbib": "KO",
  "url_add_sclib": "KO",
  "num_citations": "KO",
  "citedby_url": "KO",
  "url_related_articles": "KO",
  "eprint_url": "KO"
})

total = 1
for file in files:
    with open("./{}/{}".format(file_path,file), "r") as jsonFile:
        base = dict({ 'id': total })
        # https://favtutor.com/blogs/merge-dictionaries-python
        parsed = default_schema | base | json.load(jsonFile)
        list_of_files.append(parsed)
        total += 1

data_file = open('{}'.format(filename), 'w')
csv_writer = csv.writer(data_file)

count = 0
for data in list_of_files:
    df = pd.json_normalize(data, sep='_')
    row = df.to_dict(orient='records')[0]

    if count == 0:
        header = row.keys()
        csv_writer.writerow(header)
        count += 1

    csv_writer.writerow(row.values())

data_file.close()

print("{} row(s)".format(total -1 ))
