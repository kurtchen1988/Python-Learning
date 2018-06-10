# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class JdspiderPipeline(object):
    # Pipeline类，负责对数据库操作
    def __init__(self, mongo_uri, mongo_db):
        '''
        初始方法，定义mongodb的url和数据库变量
        :param mongo_uri:
        :param mongo_db:
        '''
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        '''
        类方法，从settings文件内拿到mangodb的设置信息
        :param crawler: 爬取类
        :return: cls实例
        '''
        return cls(mongo_uri=crawler.settings.get('MONGO_URI'), mongo_db=crawler.settings.get('MONGO_DB'))

    def open_spider(self, spider):
        '''
        开启爬虫方法，连接mongodb
        :param spider: 爬虫超类
        :return: None
        '''
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        '''
        处理item的方法，把item作为字典放入mongodb的集合内
        :param item:
        :param spider: 爬虫超类
        :return:
        '''
        self.db[item.collection].insert(dict(item))
        return item

    def close_spider(self, spider):
        '''
        爬取完成后关闭爬虫
        :param spider: 爬虫超类
        :return:
        '''
        self.client.close()