import scrapy
from demo.items import DemoItem
import re


class MySpider(scrapy.Spider):
	name = 'DemoSpider'
	start_urls = [
	'https://feebee.com.tw/s/電風扇/?sort=d&mode=l&ptab=0&page=1',
	'https://feebee.com.tw/s/電風扇/?sort=d&mode=l&ptab=0&page=2',
	'https://feebee.com.tw/s/電風扇/?sort=d&mode=l&ptab=0&page=3',
	'https://feebee.com.tw/s/電風扇/?sort=d&mode=l&ptab=0&page=4',
	'https://feebee.com.tw/s/電風扇/?sort=d&mode=l&ptab=0&page=5'
	]

	def parse(self,response):
		try:
			data = response.body.decode()
			selector = scrapy.Selector(text = data)
			total = selector.xpath('//*[@id="list_view"]/li[@class = "pure-g items"]')
			for SaleItem in total:
				item = DemoItem()
				item['title'] = total.xpath('./span/a/h3/text()').extract()
				item['price'] = total.xpath('./span/ul/li[@class = "price ellipsis xlarge"]/text()').extract()
				#item['priceRange'] = total.xpath('./span/div[@class="product_group_price price ellipsis xlarge"]/text()').extract()
				yield item
		except Exception as err:
			print(err)
