from scrapy import cmdline

cmdline.execute("scrapy crawl DemoSpider -s LOG_ENABLED=False".split())