import scrapy
from demo.items import DemoItem


class MySpider(scrapy.Spider):
	name = 'DemoSpider'
	findItem = input('請輸入產品名稱:')
	findPage = input('請輸入查詢頁數:')
	url = 'https://feebee.com.tw/s/' + findItem +'/?sort=d&mode=l&ptab=0&page='
	start_urls = []
	for i in range(1,int(findPage)+1):
		start_urls.append(url+str(i))

	def parse(self,response):
		try:
			data = response.body.decode()
			selector = scrapy.Selector(text = data)
			total = selector.xpath('//*[@id="list_view"]/li[@class = "pure-g items"]')
			for SaleItem in total:
				item = DemoItem()
				item['title'] = total.xpath('./span/a/h3/text()').extract()
				item['price'] = total.xpath('./span/ul/li[@class = "price ellipsis xlarge"]/text()').extract()
				yield item
		except Exception as err:
			print(err)
