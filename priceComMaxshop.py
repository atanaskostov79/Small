from urllib.request import urlopen
import json
import pymongo
import csv 
from fuzzywuzzy import fuzz


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Bgel"]
bgel = mydb["products"]
maxshop = mydb["maxshop_o"]
# bg = bgel.find().limit( 20 )
bg = bgel.find()

for x in bg:
    bgName = x['name']
    
    for z in maxshop.find():
        Token_Sort_Ratio = fuzz.token_sort_ratio(bgName,z['name'])

        if Token_Sort_Ratio ==100: 

            

            if x['end_price'] != z['price']:
                print(bgName, x['end_price'], z['name'], z['price'])
                with open(r'docmaxshop.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([bgName,x['end_price'],  z['price'], x['end_price'] -   z['price']])
                
                