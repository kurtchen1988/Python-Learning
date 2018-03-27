import urllib.request
import scrapy
from urllib import parse,request
from lxml import etree
import re
import json
#test git

class testPachong:

    def huati(self):

        topicOne = urllib.request.urlopen("https://www.zhihu.com/topics").read().decode("utf-8","ignore")

        htmlone = etree.HTML(topicOne)
        topicOK = htmlone.xpath('//strong/text()')
        urlOK = htmlone.xpath('//div[@class="blk"]/a[@target="_blank"]/@href')
        classOK = htmlone.xpath('//li[@class="zm-topic-cat-item"]/a/text()')
        classidOK=htmlone.xpath('//li[@class="zm-topic-cat-item"]/@data-id')
        pat='<strong>(.*?)</strong>'#话题
        pat2='<a target="_blank" href="(/topic/.*?)">'#话题详细url
        pat3 = '<a target="_blank" href="/topic/(.*?)">'#话题id
        pat4 = '<li class="zm-topic-cat-item" .*?><.*?>(.*?)</a></li>'#话题分类
        pat5 = '<li class="zm-topic-cat-item" data-id="(.*?)">'#话题分类id
        topic=re.compile(pat).findall(topicOne)
        urltopic=re.compile(pat2).findall(topicOne)
        topicid = re.compile(pat3).findall(topicOne)
        topicclass = re.compile(pat4).findall(topicOne)
        classid = re.compile(pat5).findall(topicOne)
        #话题分类 https://www.zhihu.com/topics#%E8%BF%90%E5%8A%A8   格式是https://www.zhihu.com/topics#+topicclass
        #详细话题url： https://www.zhihu.com/topic/19555490    格式是https://www.zhihu.com+urltopic

        #print(topic)
        #print(topicOK)
        #print(urltopic)
        #print(urlOK)
        #print(topicid)
        #print(classOK)
        #print(topicclass)
        #print(classidOK)
        #print(classid)

        para={'params':'{"topic_id":'+str(classid[0])+',"offset":80,"hash_id":""}',
            'method':'next'} #下一页的话题参数，用offset控制。offset就是20的倍数

        #print(para)

        realpara=urllib.parse.urlencode(para) #把参数封装

        #print(realpara)

        headers = {
            "Accept": "*/*",
            #"Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": '__DAYU_PP=mIAzqR6JjZJIV3AmU62v2ae19319dc81; q_c1=2f36189ed07842fea5d63abcf6dcfe6c|1521378566000|1521378566000; capsion_ticket="2|1:0|10:1521554442|14:capsion_ticket|44:M2IyYzBlYjY2NWI4NGQ0Y2I3NmZmMzZkYzhkMTgxZTk=|6923e50d6edf43e519899682e589376d813babd22d76629d016fb6db32874305"; _zap=34f289cd-73fc-4362-a6fa-5c39b0c71f35; r_cap_id="ZDc5ZmZlZGY4MDgwNGZjMzhkYzM3MTJiZTc0MmQ5ZDg=|1521561292|eee96888d4bc168d30324208e0b00a96d750374e"; cap_id="NjM1MWJlY2QwMGY5NGJlMGE1NjVjYTZhNzNhMjNmNjA=|1521561292|a076be34c57e4a383bbb0f177db96b3224cecfd8"; __utma=51854390.1141490050.1521384369.1521556000.1521556000.6; __utmz=51854390.1521384369.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/topics; l_cap_id="MmZhMzdhYTRkYzRhNDZmMGEzZDg2YzgyM2VkZmUyMDM=|1521561292|3a4e77d02b1e1031f6dac87af28b464ecc5ce90d"; d_c0="AEBr7njMTw2PTg-BnKIjeG7KuLINqK1ENFo=|1521473500"; _xsrf=b346d3a1d11d099f8a5fd07b9b77b2d8; __utmc=51854390; __utmv=51854390.000--|2=registration_date=20180318=1^3=entry_date=20180320=1',
            "Host": "www.zhihu.com",
            "Referer": "https://www.zhihu.com/topics",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.3",
            "X-Requested-With": "XMLHttpRequest",
            "X-Xsrftoken": "b346d3a1d11d099f8a5fd07b9b77b2d8"
        }

        sub_topic_url = 'https://www.zhihu.com/node/TopicsPlazzaListV2'

        abc=urllib.request.Request(url=sub_topic_url, headers=headers, data=bytes(realpara, encoding='utf-8'))
        #通过post方法拿到下一页的话题id
        cde=urllib.request.urlopen(abc)
        res=cde.read().decode("utf-8")
        pat6='topic./(.*?)..>'
        moreID = re.compile(pat6).findall(res)
        #print(moreID)

        topicdetail=urllib.request.urlopen("https://www.zhihu.com"+str(urltopic[0])).read().decode("utf-8")
        htmltwo=etree.HTML(topicdetail)

        question=htmltwo.xpath('//div[@itemprop="zhihu:question"]/a[@data-za-detail-view-element_name="Title"]/text()')#问题全称
        questionurl=htmltwo.xpath('//div[@itemprop="zhihu:question"]/meta[@itemprop="url"]/@content')#问题链接
        patQuestionID='https://www.zhihu.com/question/(.*?)'
        patafterID='after_id=(.*?)&'

        article = htmltwo.xpath('//div[@class="ContentItem ArticleItem"]/h2/a/text()')#文章名
        articleurl=htmltwo.xpath('//div[@class="ContentItem ArticleItem"]/h2/a/@href')#文章链接

        questionID=re.compile(patQuestionID).findall(questionurl[1])
        afterID=re.compile(patafterID).findall(topicdetail)

        #print(question)
        #print(questionurl)
        #print(questionID)
        #print(article)
        #print(articleurl)
        #print(afterID)
        #print(('http:'+str(articleurl[0])))

        nextpara = {
                'include': 'data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.content,'
                           'relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[?(target.type=topic_s'
                           'ticky_module)].target.data[?(target.type=answer)].target.is_normal,comment_count,voteup_count,'
                           'content,relevant_info,excerpt.author.badge[?(type=best_answerer)].topics;data[?(target.type='
                           'topic_sticky_module)].target.data[?(target.type=article)].target.content,voteup_count,commen'
                           't_count,voting,author.badge[?(type=best_answerer)].topics;data[?(target.type=topic_sticky_mo'
                           'dule)].target.data[?(target.type=people)].target.answer_count,articles_count,gender,follower'
                           '_count,is_followed,is_following,badge[?(type=best_answerer)].topics;data[?(target.type=answe'
                           'r)].target.content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[?('
                           'target.type=answer)].target.author.badge[?(type=best_answerer)].topics;data[?(target.type=ar'
                           'ticle)].target.content,author.badge[?(type=best_answerer)].topics;data[?(target.type=question'
                           ')].target.comment_count',
                'limit': '5',
                'after_id': '4479.08340'
                }# 下一页的话题参数，用limit和after_id控制

        # print(para)

        nextrealpara = urllib.parse.urlencode(nextpara)  # 把参数封装

        # print(realpara)

        next_headers = {
            "Accept": "application/json, text/plain, */*",
             #"Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "authorization":"oauth c3cef7c66a1843f8b3a9e6a1e3160e20",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": '__DAYU_PP=mIAzqR6JjZJIV3AmU62v2ae19319dc81; q_c1=2f36189ed07842fea5d63abcf6dcfe6c|1521378566000|1521378566000; capsion_ticket="2|1:0|10:1521554442|14:capsion_ticket|44:M2IyYzBlYjY2NWI4NGQ0Y2I3NmZmMzZkYzhkMTgxZTk=|6923e50d6edf43e519899682e589376d813babd22d76629d016fb6db32874305"; _zap=34f289cd-73fc-4362-a6fa-5c39b0c71f35; r_cap_id="ZDc5ZmZlZGY4MDgwNGZjMzhkYzM3MTJiZTc0MmQ5ZDg=|1521561292|eee96888d4bc168d30324208e0b00a96d750374e"; cap_id="NjM1MWJlY2QwMGY5NGJlMGE1NjVjYTZhNzNhMjNmNjA=|1521561292|a076be34c57e4a383bbb0f177db96b3224cecfd8"; __utma=51854390.1141490050.1521384369.1521556000.1521556000.6; __utmz=51854390.1521384369.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/topics; l_cap_id="MmZhMzdhYTRkYzRhNDZmMGEzZDg2YzgyM2VkZmUyMDM=|1521561292|3a4e77d02b1e1031f6dac87af28b464ecc5ce90d"; d_c0="AEBr7njMTw2PTg-BnKIjeG7KuLINqK1ENFo=|1521473500"; _xsrf=b346d3a1d11d099f8a5fd07b9b77b2d8; __utmc=51854390; __utmv=51854390.000--|2=registration_date=20180318=1^3=entry_date=20180320=1',
            "Host": "www.zhihu.com",
            "Referer": "https://www.zhihu.com/topic/19563451",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.3",
            "x-udid":"APBvzZ6uUw2PTunjl2NE4hNTFng78JkWYGo="
        }



        nextpage_url = 'https://www.zhihu.com/api/v4/topics/19563451/feeds/top_activity?'

        #print(nextpage_url+nextrealpara)

        nextartiur = urllib.request.Request(url=nextpage_url+nextrealpara, headers=next_headers)
        #用get方法
        nextal = urllib.request.urlopen(nextartiur)
        nextarti = nextal.read().decode("utf-8")
        #拿到下一页的源码

        #print(nextarti)

        nextactualpat='"next": "(.*?)",'

        #potest=re.compile(article)
        nextactual=re.compile(nextactualpat).findall(nextarti) #下一页url

        print(nextactual)

        nexttitlepat='"title": "(.*?)"'

        nexttitle=re.compile(nexttitlepat).findall(nextarti)

        #print(nexttitle)

        nextQuestionIDpat = '"type": "question", "id": (.*?)}'

        nextQuestionID = re.compile(nextQuestionIDpat).findall(nextarti)

        #print(nextQuestionID)

        nextarticonpat = '"url": "(http://zhuanlan.zhihu.com/p/.*?)",'

        nextArticon = re.compile(nextarticonpat).findall(nextarti)

        #print(nextArticon)

        #https://www.zhihu.com/question/269477116

        #nextPat =

        #articledetail=urllib.request.urlopen('http:'+str(articleurl[0])).read().decode("utf-8")
        #<div class="RichText PostIndex-content av-paddingSide av-card">

        #questiondetail=urllib.request.urlopen(questionurl[0]).read().decode("utf-8")

        question_headers = {
            "Accept": "application/json, text/plain, */*",
             #"Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "authorization":"oauth c3cef7c66a1843f8b3a9e6a1e3160e20",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": '__DAYU_PP=mIAzqR6JjZJIV3AmU62v2ae19319dc81; q_c1=2f36189ed07842fea5d63abcf6dcfe6c|1521378566000|1521378566000; capsion_ticket="2|1:0|10:1521554442|14:capsion_ticket|44:M2IyYzBlYjY2NWI4NGQ0Y2I3NmZmMzZkYzhkMTgxZTk=|6923e50d6edf43e519899682e589376d813babd22d76629d016fb6db32874305"; _zap=34f289cd-73fc-4362-a6fa-5c39b0c71f35; r_cap_id="ZDc5ZmZlZGY4MDgwNGZjMzhkYzM3MTJiZTc0MmQ5ZDg=|1521561292|eee96888d4bc168d30324208e0b00a96d750374e"; cap_id="NjM1MWJlY2QwMGY5NGJlMGE1NjVjYTZhNzNhMjNmNjA=|1521561292|a076be34c57e4a383bbb0f177db96b3224cecfd8"; __utma=51854390.1141490050.1521384369.1521556000.1521556000.6; __utmz=51854390.1521384369.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/topics; l_cap_id="MmZhMzdhYTRkYzRhNDZmMGEzZDg2YzgyM2VkZmUyMDM=|1521561292|3a4e77d02b1e1031f6dac87af28b464ecc5ce90d"; d_c0="AEBr7njMTw2PTg-BnKIjeG7KuLINqK1ENFo=|1521473500"; _xsrf=b346d3a1d11d099f8a5fd07b9b77b2d8; __utmc=51854390; __utmv=51854390.000--|2=registration_date=20180318=1^3=entry_date=20180320=1',
            "Host": "www.zhihu.com",
            "Referer": "https://www.zhihu.com/question/269169798",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.3",
            "x-udid":"APBvzZ6uUw2PTunjl2NE4hNTFng78JkWYGo=",
            "X-Requested-With": "XMLHttpRequest",
            "X-Xsrftoken": "b346d3a1d11d099f8a5fd07b9b77b2d8"
        }

        questionpara = {
            'include': 'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_det'
                       'ail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editab'
                       'le_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_'
                       'info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_no'
                       'thelp,upvoted_followees;data[*].mark_infos[*].url;data[*].author.follower_count,badge[?(type=bes'
                       't_answerer)].topics',
            'limit': '5',
            'offset': '10',
            'sort_by':'default'
        }

        questionrealpara=urllib.parse.urlencode(questionpara)
        #print(questionrealpara)
        questionSecUrl="https://www.zhihu.com/api/v4/questions/269169798/answers?"

        processquestion=urllib.request.Request(url=questionSecUrl+questionrealpara, headers=question_headers)
        processquestio=urllib.request.urlopen(processquestion)
        processquesti=processquestio.read().decode("utf-8")

        answerpat='"content": "(.*?)",'
        answer=re.compile(answerpat).findall(processquesti)
        #print(processquesti)
        print(answer)

    def articleLink(self):

        pass

if __name__ == '__main__':
    a = testPachong()
    a.huati()
