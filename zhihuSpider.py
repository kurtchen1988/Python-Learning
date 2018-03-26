import pymysql
import urllib.request
from lxml import etree
import re
import json


class zhihuSpider:

    pages=5
    #每个话题抓取几页内容

    cleanCookie = '__DAYU_PP=mIAzqR6JjZJIV3AmU62v2ae19319dc81; q_c1=2f36189ed07842fea5d63abcf6dcfe6c|1521378566000|15213' \
                  '78566000; capsion_ticket="2|1:0|10:1521554442|14:capsion_ticket|44:M2IyYzBlYjY2NWI4NGQ0Y2I3NmZmMzZkYz' \
                  'hkMTgxZTk=|6923e50d6edf43e519899682e589376d813babd22d76629d016fb6db32874305"; _zap=34f289cd-73fc-4362' \
                  '-a6fa-5c39b0c71f35; r_cap_id="ZDc5ZmZlZGY4MDgwNGZjMzhkYzM3MTJiZTc0MmQ5ZDg=|1521561292|eee96888d4bc168' \
                  'd30324208e0b00a96d750374e"; cap_id="NjM1MWJlY2QwMGY5NGJlMGE1NjVjYTZhNzNhMjNmNjA=|1521561292|a076be34c' \
                  '57e4a383bbb0f177db96b3224cecfd8"; __utma=51854390.1141490050.1521384369.1521556000.1521556000.6; __ut' \
                  'mz=51854390.1521384369.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/topics; l_cap_' \
                  'id="MmZhMzdhYTRkYzRhNDZmMGEzZDg2YzgyM2VkZmUyMDM=|1521561292|3a4e77d02b1e1031f6dac87af28b464ecc5ce90d"; ' \
                  'd_c0="AEBr7njMTw2PTg-BnKIjeG7KuLINqK1ENFo=|1521473500"; _xsrf=b346d3a1d11d099f8a5fd07b9b77b2d8; __utm' \
                  'c=51854390; __utmv=51854390.000--|2=registration_date=20180318=1^3=entry_date=20180320=1',


    def __init__(self):
        pass

    def get_topic(self):
        '''得到话题信息'''

        firstPage = self.get_URLCode("https://www.zhihu.com/topics")

        topicpat = '<strong>(.*?)</strong>'  # 话题
        #pat2 = '<a target="_blank" href="(/topic/.*?)">'  # 话题详细url
        tidpat = '<a target="_blank" href="/topic/(.*?)">'  # 话题id
        classpat = '<li class="zm-topic-cat-item" .*?><.*?>(.*?)</a></li>'  # 话题分类
        classIDpat = '<li class="zm-topic-cat-item" data-id="(.*?)">'  # 话题分类id

        topicClass = re.compile(classpat).findall(firstPage)

        for j in range(0, len(topicClass)):

            topicurl = "https://www.zhihu.com/topics#" + urllib.parse.quote(topicClass[j])
            referurl = "https://www.zhihu.com/topics"
            print(topicurl)
            topicpage = self.get_URLCode(topicurl)
            topicOne = urllib.request.urlopen(topicurl).read().decode("utf-8", "ignore")

            for k in range(0, self.pages):
                if(k==0):
                    topic = re.compile(topicpat).findall(topicpage)
                    print(topic)
                    topicID = re.compile(tidpat).findall(topicpage)
                    classID = re.compile(classIDpat).findall(topicpage)
                    for i in range(0, len(topic)):
                        topicDic = {"id": 0, "titlename": topic[i], "tid": topicID[i], "class": topicClass[j]}
                        # id为自增量，传入任意数字即可.默认首页为第一个标题
                        self.write_to_DB(topicDic, "topic")
                else:
                    para = {'params': '{"topic_id":' + classID[j] + ',"offset":'+ str(k*20) +',"hash_id":""}', 'method': 'next'}  # 下一页的话题参数，用offset控制。offset就是20的倍数
                    print(para)
                    realpara = urllib.parse.urlencode(para)
                    topicheader = self.get_header(self.cleanCookie, referurl)
                    next_page_url = 'https://www.zhihu.com/node/TopicsPlazzaListV2'

                    abc = urllib.request.Request(url=next_page_url, headers=topicheader,data=bytes(realpara, encoding='utf-8'))
                    # 通过post方法拿到下一页的话题id
                    cde = urllib.request.urlopen(abc)
                    res = cde.read().decode("utf-8")
                    pat6 = 'topic./(.*?)..>'
                    moreID = re.compile(pat6).findall(res)



        pass

    def get_header(self, cookie, refer):
        '''处理所有request的头信息'''
        request_headers = {
            "Accept": "application/json, text/plain, */*",
            # "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "authorization": "oauth c3cef7c66a1843f8b3a9e6a1e3160e20",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": cookie,
            "Host": "www.zhihu.com",
            "Referer": str(refer),
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.3",
            "x-udid": "APBvzZ6uUw2PTunjl2NE4hNTFng78JkWYGo="
        }
        return request_headers

    def get_nextTopicPara(self, after_id):
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
            'after_id': after_id
        }
        return nextpara

    def get_URLCode(self, url):

        return urllib.request.urlopen(url).read().decode("utf-8","ignore")

    def write_to_DB(self, dict, type):
        #self.conn = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="zhihu")
        if(type=="topic"):
            print(dict)
            #sql="INSERT into topic(id, titlename, tid, class) VALUES ("+dict["id"]+dict["titlename"]+","+dict["tid"]+","+dict["class"]+")"
        elif(type=="artlink"):
            print(dict)
            #sql = "INSERT into artlink(artid, tid, title, link) VALUES (" + dict["artid"] + "," + dict["tid"] + "," + dict[
            #    "title"] + dict["link"] +")"
        elif(type=="article"):
            print(dict)
            #sql = "INSERT into article(id, title, author, aid, content, link) VALUES (" + dict["id"] + "," + dict["title"] + "," + dict[
            #    "author"] + "," + dict["aid"] + "," + dict["content"] + "," + dict["link"] + ")"
        elif(type=="question"):
            print(dict)
            #sql = "INSERT into question(id, title, detail, aid, content, link) VALUES (" + dict["id"] + "," + dict["title"] + "," + dict[
            #    "detail"] + "," + dict["aid"] + "," + dict["content"] + "," + dict["link"] + ")"
        elif(type=="answer"):
            print(dict)
            #sql = "INSERT into answer(id, author, content, askid) VALUES (" + dict["id"] + "," + dict["author"] + "," + dict[
            #    "content"] + "," + dict["askid"] + ")"
        #self.conn.commit()
        #self.conn.close()

    def test(self):
        a={"aa":1,"bb":2}
        print(a["aa"])

if __name__ == '__main__':
    a = zhihuSpider()
    a.get_topic()