import time
import pymongo
import requests
import json
import pycurl
import urllib.request

URL = "http://oc3.sprintex.bg/api/rest_admin/categories/level/3"
headers = {'X-Oc-Restadmin-Id': 'qzJ76QaBLY41TwSyymP5BNgQhPBzqtd1', 'Content-Type': 'application/json'}
headers1 = {'X-Oc-Restadmin-Id': 'qzJ76QaBLY41TwSyymP5BNgQhPBzqtd1', 'Content-Type': 'application/json', "Content-Type": "multipart/form-data"}
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Trapi"]
r = requests.get(URL, data=json.dumps({}), headers=headers)
data = r.json()['data']

for x in data:
    print("|" + x['name'] + " - " + str(x['category_id']))
    if len( x['categories']) > 0:
        for subcat in x['categories'] :
            print("|--> {} - {}".format(subcat['name'], subcat['category_id']))


cat = int(input("Cat : "))
colW = db["IzotPcW"]

def uploadLaptops():
    colX = db["IzotLaptopsX"]
    for x in colX.find():
        # i = i + 1

        myquery =  {"title": x['brand'] + " " + x['model']}
        mydoc = colW.find(myquery)
        for w in mydoc:
            # Download files
            filename = x['model']
            filename = filename.replace(' ', '-')
            filename = filename.replace('/', '-')
            # print(filename)
            # urllib.request.urlretrieve(w['img'], "./img/" + filename + ".jpg")
            time.sleep(1)
            save = {
                "model": x['model'],
                "quantity": 300,
                "price": float(x['price']),
                "tax_class_id": 1,
                "manufacturer_id": 20,
                "sku": x['model'],
                "keyword": x['brand'] + " " + x['model'] ,
                "status": 1,
                "points": 0,
                "reward": 0,

                "other_images": [

                ],
                "product_description": [
                    {
                        "language_id": 2,
                        "name": x['brand'] + " " + x['model'],
                        "description": x['Desc'],
                        "meta_title": "Meta title of the product",
                        "meta_description": "Meta description of the product",
                        "meta_keyword": "demo, keyword, demo2",
                        "tag": "Products tag, comma separeted"
                    }
                ],
                "product_category": [cat],
                "product_attribute": [
                    {
                        "attribute_id": 18,
                        "product_attribute_description": [
                            {
                                "text": x['CPU'],
                                "language_id": 2
                            }
                        ]
                    },
                    {
                        "attribute_id": 19,
                        "product_attribute_description": [
                            {
                                "text": x['RAM'],
                                "language_id": 2
                            }
                        ]
                    },
                    {
                        "attribute_id": 22,
                        "product_attribute_description": [
                            {
                                "text": x['screen_size'],
                                "language_id": 2
                            }
                        ]
                    },
                    {
                        "attribute_id": 21,
                        "product_attribute_description": [
                            {
                                "text": x['ODD'],
                                "language_id": 2
                            }
                        ]
                    },
                    {
                        "attribute_id": 23,
                        "product_attribute_description": [
                            {
                                "text": x['grade'],
                                "language_id": 2
                            }
                        ]
                    },
                    {
                        "attribute_id": 24,
                        "product_attribute_description": [
                            {
                                "text": x['grade_barrery'],
                                "language_id": 2
                            }
                        ]
                    }
                ],
            }
            URL = 'http://pc-ita.com/api/rest_admin/products'
            t = requests.post(URL, json.dumps(save), headers=headers)
            data = t.json()['data']
            print (data['id'])

            URLImage = 'http://pc-ita.com/api/rest_admin/products/' + str(data['id']) + '/images'


            crl = pycurl.Curl()
            crl.setopt(crl.URL, URLImage)
            crl.setopt(crl.HTTPHEADER, ['accept: application/json', 'X-Oc-Restadmin-Id: WGSkcyx8LavOE1N8tOuHrEl2nQNSjYHa',
                                        'Content-Type: multipart/form-data'])
            crl.setopt(crl.HTTPPOST, [
                ('file', (
                    # Upload the contents of the file
                    crl.FORM_FILE, "./img/" + filename + ".jpg",
                    crl.FORM_CONTENTTYPE, 'image/jpeg'
                )),
            ])
            crl.perform()
            crl.close()
            break


def uploadPC():
    # i = 0
    colX = db["IzotPcX"]

    for x in colX.find():
        # i = i + 1

        myquery =  {"title": x['brand'] + " " + x['model'] + " " + x['Case']}
        mydoc = colW.find(myquery)

        for w in mydoc:
            # Download files
            filename = x['model'] + x['Case']
            filename = filename.replace(' ', '-')
            filename = filename.replace('/', '-')
            print(filename)
            urllib.request.urlretrieve(w['img'], "./img/" + filename + ".jpg")
            time.sleep(1)

            save = {
                "model": x['model'],
                "quantity": 300,
                "price": float(x['price']),
                "tax_class_id": 1,
                "manufacturer_id": 20,
                "sku":  x['model'],
                "keyword": x['brand'] + " " + x['model'] + " " + x['Case'],
                "status": 1,
                "points": 0,
                "reward": 0,
                # "image": w['img'],
                "other_images": [

                ],
                "product_description": [
                    {
                        "language_id": 2,
                        "name": x['brand'] + " " + x['model'] + " " + x['Case'],
                        "description": x['Desc'],
                        "meta_title": "Meta title of the product",
                        "meta_description": "Meta description of the product",
                        "meta_keyword": "demo, keyword, demo2",
                        "tag": "Products tag, comma separeted"
                    }
                ],
                "product_category": [cat],
                "product_attribute": [
                    {
                        "attribute_id": 12,
                        "product_attribute_description": [
                            {
                                "text": x['CPU'],
                                "language_id": 2
                            }
                        ]
                    },
                    {
                        "attribute_id": 13,
                        "product_attribute_description": [
                            {
                                "text": x['RAM'],
                                "language_id": 2
                            }
                        ]
                    },
                    {
                        "attribute_id": 16,
                        "product_attribute_description": [
                            {
                                "text": x['Case'],
                                "language_id": 2
                            }
                        ]
                    },
                    {
                        "attribute_id": 17,
                        "product_attribute_description": [
                            {
                                "text": x['ODD'],
                                "language_id": 2
                            }
                        ]
                    }
                ],
            }
            URL = 'http://pc-ita.com/api/rest_admin/products'
            t = requests.post(URL, json.dumps(save), headers=headers)
            data = t.json()['data']
            print (data['id'])

            URLImage = 'http://pc-ita.com/api/rest_admin/products/' + str(data['id']) + '/images'


            crl = pycurl.Curl()
            crl.setopt(crl.URL, URLImage)
            crl.setopt(crl.HTTPHEADER, ['accept: application/json', 'X-Oc-Restadmin-Id: WGSkcyx8LavOE1N8tOuHrEl2nQNSjYHa',
                                        'Content-Type: multipart/form-data'])
            crl.setopt(crl.HTTPPOST, [
                ('file', (
                    # Upload the contents of the file
                    crl.FORM_FILE, "./img/" + filename + ".jpg",
                    crl.FORM_CONTENTTYPE, 'image/jpeg'
                )),
            ])
            crl.perform()
            crl.close()

    # print(str(i))
