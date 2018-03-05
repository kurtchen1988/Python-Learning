# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        conn=pymysql.connect(host="127.0.0.1", user="root",passwd="root", db="dd", charset="utf8")
        for i in range(0,len(item["title"])):
            title=item["title"][i]
            link=item["link"][i]
            comment=item["comment"][i]

            #print(title+":"+link+":"+comment)
            sql= "insert into goods(title, link, comment) VALUES ('"+title+"','"+link+"','"+comment+"')"
            #print(sql)
            try:
                conn.query(sql)
            except Exception as err:
                print(err)
        conn.close()
        return item
