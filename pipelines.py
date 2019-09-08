# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DemoPipeline(object):
    count = 0
    def process_item(self, item, spider):
        DemoPipeline.count += 1
        try:
        	if DemoPipeline.count == 1:
        		fobj = open("price.txt","wt")
        	else:
        		fobj = open("price.txt","at")
        	for i,j in zip(item['title'],item['price']):
        		fobj.write(str(i)+","+str(j)+'\n')
        		print("item:",str(i),",","price:",str(j))
        	fobj.close()
        except Exception as err:
        	print(err)
        return item
