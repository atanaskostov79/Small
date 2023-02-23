import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
at = myclient["Bgel"]
atc = at["athlets"]
pbc = at["maxshop"]
pbco = at["maxshop_o"]
pbco.drop()

for x in pbc.find():
  myquery = { "name": x['name'] }  
  if pbco.find(myquery).count() == 0:
    ins = pbco.insert_one(x)
  