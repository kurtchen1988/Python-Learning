# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class MongoPipeline(object):
    ''' 完成MongoDB数据库对Item信息的存储'''

    def __init__(self, mongo_uri, mongo_db):
        '''对象初始化'''
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        '''通过依赖注入方式实例化当前类，并返回，参数是从配置文件获取MongoDB信息'''
        return cls(mongo_uri=crawler.settings.get('MONGO_URI'), mongo_db=crawler.settings.get('MONGO_DB'))

    def open_spider(self, spider):
        '''Spider开启自动调用此方法，负责连接MongoDB，并选择数据库'''
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        '''选择对应集合并写入Item信息'''
        self.db[item.collection].insert(dict(item))
        return item

    def close_spider(self, spider):
        '''Spider关闭时自动调用，负责关闭MongoDB的连接'''
        self.client.close()