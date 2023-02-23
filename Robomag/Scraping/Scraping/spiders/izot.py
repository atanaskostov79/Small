from time import strftime
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import PowerbeautyscrapyItem
from bs4 import BeautifulSoup

class izot(CrawlSpider):
    
        name = "izot"
        allowed_domains = ['izotcomputers.com']
        start_urls = ["https://izotcomputers.com/"]
        base_url = 'https://izotcomputers.com/'
# deny = 'https://izotcomputers.com/en/',
        rules = [Rule(LinkExtractor(allow='https://izotcomputers.com/',  restrict_css=('div.menu', 'section#products')), callback='parseIzot', follow=True)]
        def optionsOC(value, name):
            res = {}
            i = 0
            for v in value:
                res[v] = name[i]
                i = i+1
            print(res)
            return res

        def parseIzot(self, response):
           
                try:
                    options = izot.optionsOC(response.css('dt[class=name]::text').getall() ,response.css('dd[class=value]::text').getall())
                    product = PowerbeautyscrapyItem()
                    product['name'] = response.css('h1.h1::text').get()
                
                    product['price'] = float(izot.cleanTxt(response.css('span[itemprop=price]::text').get()))
                    product['categories'] = response.css('span[itemprop=name]::text').getall()[-2] 
                    product['product_id'] = int(izot.cleanTxt(response.css('span[class=product_product_id]::text').get()))
                    product['options'] =options

                    product['description'] = response.css('div[itemprop=description] p::text').get()  #HalfWorling need's some soup ;)
                    product['distributor'] = 'izotcomputers.com'
                    product['images'] = response.css('img[data-image-large-src]::attr(src)').getall()
                    product['time_of_download'] = strftime("%d-%m-%Y")
                    yield product
                except:
                    print("price is null")                
                

        def cleanTxt( text):
        
            try:
                    res = str(text)
                    res = re.sub("\xa0лв.", '', res)
                    res = re.sub(",", '.', res)
                    res = re.sub('Арт. №: ', '', res)
                    return res
            except:
                    print("Debug", res)

