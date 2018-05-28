# -*- coding: utf-8 -*-
import pymysql
from scrapy.exceptions import DropItem

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        if item['name'] == None:
            raise DropItem("Drop item found: %s" % item)
        else:
            return item

class MysqlPipeline(object):
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.db = None
        self.cursor = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get("MYSQL_HOST"),
            database=crawler.settings.get("MYSQL_DATABASE"),
            user=crawler.settings.get("MYSQL_USER"),
            password=crawler.settings.get("MYSQL_PASS"),
            port=crawler.settings.get("MYSQL_PORT")
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8', port=self.port)
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        sql = "insert into danginfo(name,price,pic,author,publisher,comments, pubdate, description) values('%s','%s','%s','%s','%s','%s', '%s', '%s')"%(item['name'],item['price'],item['pic'],item['author'],item['publisher'],item['comments'], item['pubdate'],item['description'])
        print(sql)
        self.cursor.execute(sql)
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.db.close()
