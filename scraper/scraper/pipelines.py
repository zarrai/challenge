# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from word2number import w2n

class ScraperPipeline(object):
    """
    Saves Item to the database
    """
    def process_item(self, item, spider):
        item.save()
        return item

class PropertyNumberPipeline(object):
    """
    Replace text for item bill_number
    """
    def process_item(self, item, spider):
        if item.get('bill_number'):
            item['bill_number'] = item['bill_number'].replace('Statement of Administration Policy: ', '').split("-")
            item['bill_number'] = item['bill_number'][0] 
            return item

class PropertyBillPipeline(object):
    """
    Replace text for item bill
    """
    def process_item(self, item, spider):
        if item.get('bill'):
            item['bill'] = item['bill'].replace('Statement of Administration Policy: ', '').split("-")
            item['bill'] = item['bill'][1] 
            return item

class PropertyLinkPipeline(object):
    """
    make complete link for item link
    """
    def process_item(self, item, spider):
        if item.get('link'):
            item['link'] = 'https://www.presidency.ucsb.edu' + item['link']
            return item