# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class DemoPipeline(object):
    count = 0
    def process_item(self, item, spider):
        DemoPipeline.count += 1
        try:
            fobj = open('output.csv','a+')
            writer = csv.writer(fobj)
            if DemoPipeline.count == 1:
                writer.writerow(['title','price'])
            else:
                for i,j in zip(item['title'],item['price']):
                    writer.writerow([str(i),str(j)])
                    print('item:',str(i),' , ','price',str(j))
        except Exception as err:
        	print(err)
        return item

