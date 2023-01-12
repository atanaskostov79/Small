from urllib.request import urlopen
import json
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Bgel"]
mycol = mydb["cats"]
url = "https://www.bgelectronics.eu/index.php?route=feed/products_json/getData&langluages[1]=1"
# url = "https://www.bgelectronics.eu/index.php?route=feed/products_json/products&languages[1]=1"
# store the response of URL
response = urlopen(url)

data_json = json.loads(response.read())
# print(data_json['categories']['1'])
for z in data_json['categories']:
    print(data_json['categories'][str(z)])
    x = mycol.insert_one(data_json['categories'][str(z)]) #e te tui mu trebeshe str(z)

