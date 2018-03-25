# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TopicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    topicID = scrapy.Field()
    topicName = scrapy.Field()
    topicClass = scrapy.Field()

    pass

class ArtLinkItem(scrapy.Item):

    artLinkTitle = scrapy.Field()
    artLinkURL = scrapy.Field()
    artLinkID = scrapy.Field()

    pass

class ArticleItem(scrapy.Item):
    articleID = scrapy.Field()
    articleTitle = scrapy.Field()
    articleURL = scrapy.Field()
    artTopID = scrapy.Field()

    pass

class Question(scrapy.Item):
    quesID = scrapy.Field()
    quesTitle = scrapy.Field()
    quesLink = scrapy.Field()
    quesDetail = scrapy.Field()
    pass


class Answer(scrapy.Item):
    ansID = scrapy.Field()
    ansAuthor = scrapy.Field()
    ansContent = scrapy.Field()
    pass