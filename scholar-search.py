from slugify import slugify
from scholarly import scholarly, ProxyGenerator
import json

#https://github.com/scholarly-python-package/scholarly

print("setting up proxy")
# Set up a ProxyGenerator object to use free proxies
# This needs to be done only once per session
pg = ProxyGenerator()
# pg.FreeProxies()

success = pg.ScraperAPI()

print("setting up proxy - done " + str(success))

scholarly.use_proxy(pg)

# Now search Google Scholar from behind a proxy
search_string = '(tdd OR "unit test*" OR "test-driven development" OR "test driven development" ) AND ( "anti-pattern*" OR "anti pattern*" OR antipattern* OR pattern* )'

search_query = scholarly.search_pubs(search_string)

print("starting search for {}".format(search_string))
for article in search_query:
    title = slugify(article['bib']['title'])
    print(title)
    with open("./results/{}.json".format(title), "w") as file:
        fill = article
        convert = json.dumps(fill)
        file.write(convert)

print("searching - done")
