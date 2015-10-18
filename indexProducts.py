import netHandler
import json
import finder


def filterLinks(file, n):

    linkStart = finder.findN(file, '<span class="item-code">', n)
    #print(linkStart)
    linkPos = file[linkStart:].find("href=")

    link = file[linkPos:linkPos + 50]
    print("Link: " + link)
    return link


with open("category.json", "r") as file:
    categories = json.loads(file.read())

#netHandler.Reader.load()
print(len(categories["categories"]))

for i in range(0, len(categories["categories"])):
    category = categories["categories"][i]
    print(category["name"])

    filterLinks(netHandler.Reader.loadCatgories(category["id"]), i)

