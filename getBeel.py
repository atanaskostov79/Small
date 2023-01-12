from urllib.request import urlopen
import json
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Bgel"]
mycol = mydb["products"]
mycol.drop()
# url = "https://www.bgelectronics.eu/index.php?route=feed/products_json/getData&langluage=bg"
url = "https://www.bgelectronics.eu/index.php?route=feed/products_json/products&languages[1]=2"
# store the response of URL
response = urlopen(url)

data_json = json.loads(response.read())
for z in data_json:
    print(z)
    
    z['end_price'] = float(z['end_price'])
    z['custumer_price'] = float(z['custumer_price'])
    z['name']  = z['description']['2']['product_name']
    print(z['description']['2']['product_name'])
    x = mycol.insert_one(z)

