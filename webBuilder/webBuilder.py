import json


with open("products.json") as productFile:
    products = json.reads(productFile.read())
print(products)