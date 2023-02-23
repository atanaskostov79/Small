from time import strftime
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import PowerbeautyscrapyItem
from bs4 import BeautifulSoup

class impacto(CrawlSpider):
    
        name = "impacto"
        allowed_domains = ['impacto.bg']
        start_urls = ['https://www.impacto.bg/']
        base_url = 'https://www.impacto.bg/'
        custom_settings = {'ITEM_PIPELINES': {'Scraping.pipelines.ImpactoPipeline': 400}}

# deny = 'https://impacto.bg/en/', , restrict_css=('div.collapse.navbar-collapse.mobile-nav', 'div.selected-items')
        rules = [Rule(LinkExtractor(allow='https://www.impacto.bg/', restrict_css=('div#navbarSupportedContent', 'div.selected-items')), callback='parseIzot', follow=True)]
        def optionsOC(value, name):
            res = {}
            i = 0
            rr = []
            for r in value:
                r = r.strip()
                if r:
                    rr.append(r)
            
            value = rr
            for v in value:
                res[v.strip()] = name[i]
                i = i+1
            print(res)
            return res

        def parseIzot(self, response):
           
                try:
                    options = impacto.optionsOC(response.css('div.characteristics-box p::text').getall() ,response.css('div.characteristics-box p span::text').getall())
                    product = PowerbeautyscrapyItem()
                    product['name'] = response.css('div.name-holder h1::text').get()
                    
                    product['price'] = float(impacto.cleanTxt(response.css('div.price-content h4::text').get().strip() + "." + response.css('div.price-content h4 sup::text').get().strip()))
                    product['categories'] = response.css('div.breadcrumb p a::text').get().strip()
                    product['product_id'] = int(response.css('div.serial-number p span::text').get().strip())
                    product['options'] =options

                    product['description'] = response.css('div.additional-characteristics p span::text').get().strip()  #HalfWorling need's some soup ;)
                    product['distributor'] = 'impacto.bg'
                    product['images'] = response.css('img.img-fluid::attr(src)').getall()
                    product['time_of_download'] = strftime("%d-%m-%Y")
                    yield product
                except:
                    print("price is null")                
                

        def cleanTxt( text):
        
            try:
                    res = str(text)
                    res = re.sub("\xa0лв.", '', res)
                    res = re.sub('Арт. №: ', '', res)
                    return res
            except:
                    print("Debug", res)

