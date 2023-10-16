import csv


file_list = []
id = 1

def build_record(
    id,
    title,
    abstract,
    authors,
    year,
    source,
    doi,
    url_for_publication,
    database
):
    return {
        'id': id,
        'title': title,
        'abstract': abstract,
        'authors': authors,
        'year': year,
        'source': source,
        'doi': doi,
        'database': database,
        'url_of_publication': url_for_publication
    }

with open("database/scholar.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        file_list.append(
            build_record(
                id,
                row['bib_title'],
                row['bib_abstract'],
                row['bib_author'],
                row['bib_pub_year'],
                row['bib_venue'],
                "preprint scholar - " + row['eprint_url'],
                row['pub_url'],
                "Google Scholar"
            )
        )
        id = id + 1

with open("database/scopus.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        file_list.append(
            build_record(
                id,
                row['Title'],
                row['Abstract'],
                row['\ufeff"Authors"'],
                row['Year'],
                row['Source'],
                row['DOI'],
                row['Link'],
                "Scopus"
            )
        )
        id = id + 1

with open("database/wos.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')
    for row in csv_reader:
        file_list.append(
            build_record(
                id,
                row['Article Title'],
                row['Abstract'],
                row['Author Full Names'],
                row['Publication Year'],
                row['Source Title'],
                row['DOI'],
                "https://doi.org/" + row['DOI'],
                "Web of Science"
            )
        )
        id = id + 1


filename = "database/merged.csv"
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