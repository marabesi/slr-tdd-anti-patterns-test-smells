import csv


file_list = []

def build_record(title, abstract, authors, year, source, doi, url_for_publication):
    return {
        'title': title,
        'abstract': abstract,
        'authors': authors,
        'year': year,
        'source': source,
        'doi': doi,
        'url_of_publication': url_for_publication
    }

with open("scopus.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        file_list.append(
            build_record(
                row['Title'],
                row['Abstract'],
                row['\ufeff"Authors"'],
                row['Year'],
                row['Source'],
                row['DOI'],
                row['Link'],
            )
        )

with open("wos.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        file_list.append(
            build_record(
                row['Article Title'],
                row['Abstract'],
                row['Author Full Names'],
                row['Publication Year'],
                row['Source Title'],
                row['DOI'],
                "https://doi.org/" + row['DOI'],
            )
        )

filename = "merged.csv"
data_file = open('{}'.format(filename), 'w')
csv_writer = csv.writer(data_file)

count = 0
for data in file_list:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1

    csv_writer.writerow(data.values())

data_file.close()

print("{} articles merged".format(len(file_list)))
