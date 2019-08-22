# -*- coding: utf-8 -*-
from scrapy import Spider, Request, Selector
from urllib.parse import quote
from dianpingsplash.items import HpItem
from scrapy_splash import SplashRequest
from dianpingsplash.config import  CSS_URL, SVG_NUM_URL, SVG_FONT_URL
script = """
function main(splash, args)
  splash.images_enabled = false
  assert(splash:go(args.url))
  assert(splash:wait(args.wait))
  js = string.format("document.querySelector('#mainsrp-pager div.form > input').value=%d;document.querySelector('#mainsrp-pager div.form > span.btn.J_Submit').click()", args.page)
  splash:evaljs(js)
  assert(splash:wait(args.wait))
  return splash:html()
end
"""
class DianpingSpider(Spider):
    name = 'dianping'
    allowed_domains = ['www.dianping.com']
    start_urls = ['https://www.dianping.com/search/keyword/2/']
    base_url = 'https://www.dianping.com/search/keyword/2/0_%E8%BD%B0%E8%B6%B4'
    def start_requests(self):
        #for keyword in self.settings.get('KEYWORDS'):
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            url = self.base_url #+ quote(keyword)
            yield SplashRequest(url, callback=self.parse, endpoint='execute',args={'lua_source': script, 'page': page, 'wait': 7})
    
    def parse(self, response):
        res = Selector(text=response.text)
        li_list = res.xpath('//*[contains(@class, "shop-all-list")]/ul/li')
        try:
            for shop in shops:
                data = parse(li, self.svg_num_url, self.svg_font_url, self.css_url)
                print("=========获取数据=============")
                print(data)
                break
                #item = HpItem()
                #店铺名称
                #item['shop_name'] = ''
                #item['address'] = ''
                #item['evaluate_star'] = ''
                #item['evaluate_total'] = ''
                #item['avg_per_consume'] = ''
        except Exception as e:
            print('Error: %s, Please Check it.' % e.args)

