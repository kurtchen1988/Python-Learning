# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import zhihuCrawl.items

class ZhihucrawlPipeline(object):
    def process_item(self, item, spider):

        if isinstance(item, zhihuCrawl.items.TopicItem):
            print(zhihuCrawl.items.TopicItem.get("topicID"))
            print(zhihuCrawl.items.TopicItem.get("topicName"))
            print(zhihuCrawl.items.TopicItem.get("topicClass"))
            print(1)
        elif isinstance(item, zhihuCrawl.zhihuCrawl.items.ArtLinkItem):
            print(2)
        elif isinstance(item, zhihuCrawl.zhihuCrawl.items.ArticleItem):
            print(3)
        elif isinstance(item, zhihuCrawl.zhihuCrawl.items.Question):
            print(4)
        elif isinstance(item, zhihuCrawl.zhihuCrawl.items.Answer):
            print(5)

        return item
