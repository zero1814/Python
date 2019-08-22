# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class DianpingItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class HpgItem(Item):
    collection = 'hp_data'
    shop_name = Field()
    address = Field()
    evaluate_star = Field()
    evaluate_total = Field()
    avg_per_consume = Field()