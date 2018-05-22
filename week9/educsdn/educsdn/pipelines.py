# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.exceptions import DropItem

class EducsdnPipeline(object):
    def process_item(self, item, spider):
        if item['price'] == None:
            raise DropItem("Drop item found: %s" % item)
        else:
            return item


class MysqlPipeline(object):
    def __init__(self,host,database,user,password,port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.db=None
        self.cursor=None

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            host = crawler.settings.get("MYSQL_HOST"),
            database = crawler.settings.get("MYSQL_DATABASE"),
            user = crawler.settings.get("MYSQL_USER"),
            password = crawler.settings.get("MYSQL_PASS"),
            port = crawler.settings.get("MYSQL_PORT")
        )

    def open_spider(self,spider):
        self.db = pymysql.connect(self.host,self.user,self.password,self.database,charset='utf8',port=self.port)
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        sql = "insert into courses(title,url,pic,teacher,time,price) values('%s','%s','%s','%s','%s','%s')"%(item['title'],item['url'],item['pic'],item['teacher'],str(item['time']),str(item['price']))
        #print(item)
        self.cursor.execute(sql)
        self.db.commit()
        return item

    def close_spider(self,spider):
        self.db.close()