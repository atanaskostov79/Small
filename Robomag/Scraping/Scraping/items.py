# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from itemloaders.processors import MapCompose, TakeFirst
import scrapy
from scrapy.loader import ItemLoader
from w3lib.util import unicode_to_str

class PowerbeautyscrapyItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    categories = scrapy.Field()
    product_id = scrapy.Field()
    options = scrapy.Field()

   
    description = scrapy.Field()
   
    distributor = scrapy.Field() 
    images = scrapy.Field()
    time_of_download = scrapy.Field()
    default_input_processor = MapCompose(unicode_to_str)
    default_output_processor = TakeFirst()
