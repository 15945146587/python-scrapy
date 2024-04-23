# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    number = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    crawler_time = scrapy.Field()
    # pass
