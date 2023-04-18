import json
from os import listdir

files = listdir("./results")

total = 0
for file in files:
    with open("./results/{}".format(file), "r") as jsonFile:
        total = total + 1
        parsed = json.load(jsonFile)
        print(parsed['bib']['title'])

print("{} document(s)".format(total))
