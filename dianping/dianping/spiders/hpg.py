# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider, Request, Selector
from dianping.items import HpgItem
from scrapy_splash import SplashRequest
from dianping.config import  CSS_URL, SVG_NUM_URL, SVG_FONT_URL
from dianping.dbclient import RedisClient
class HpgSpider(scrapy.Spider):
    name = 'hpg'
    allowed_domains = ['www.dianping.com']
    start_urls = ['http://www.dianping.com/']
    base_url = 'http://www.dianping.com/search/keyword/2/0_%E8%BD%B0%E8%B6%B4'

    def parse(self, response):
        res = Selector(text=response.text)
        shops = res.xpath('//*[contains(@id, "shop-all-list")]/ul/li')
        try:
            for shop in shops:
                data = parse(li, self.svg_num_url, self.svg_font_url, self.css_url)
                print("=========获取数据=============")
                print(data)
                redis = RedisClient()
                redis.add(data)
                #item = HpItem()
                #店铺名称
                #item['shop_name'] = ''
                #item['address'] = ''
                #item['evaluate_star'] = ''
                #item['evaluate_total'] = ''
                #item['avg_per_consume'] = ''
        except Exception as e:
            print('Error: %s, Please Check it.' % e.args)