import pymysql
import urllib.request
from lxml import etree
import re
import json
import random
import http.cookiejar


class zhihuSpider:

    topicpages=2
    #每个话题页面抓取几页内容
    articlepages=5
    #文章页面抓取几页内容

    headers = (
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36 OPR/37.0.2178.32",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.3 Safari/537.36")

    cleanCookie = '__DAYU_PP=mIAzqR6JjZJIV3AmU62v2ae19319dc81; q_c1=2f36189ed07842fea5d63abcf6dcfe6c|1521378566000|1521378566000; capsion_ticket="2|1:0|10:1521554442|14:capsion_ticket|44:M2IyYzBlYjY2NWI4NGQ0Y2I3NmZmMzZkYzhkMTgxZTk=|6923e50d6edf43e519899682e589376d813babd22d76629d016fb6db32874305"; _zap=34f289cd-73fc-4362-a6fa-5c39b0c71f35; r_cap_id="ZDc5ZmZlZGY4MDgwNGZjMzhkYzM3MTJiZTc0MmQ5ZDg=|1521561292|eee96888d4bc168d30324208e0b00a96d750374e"; cap_id="NjM1MWJlY2QwMGY5NGJlMGE1NjVjYTZhNzNhMjNmNjA=|1521561292|a076be34c57e4a383bbb0f177db96b3224cecfd8"; __utma=51854390.1141490050.1521384369.1521556000.1521556000.6; __utmz=51854390.1521384369.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/topics; l_cap_id="MmZhMzdhYTRkYzRhNDZmMGEzZDg2YzgyM2VkZmUyMDM=|1521561292|3a4e77d02b1e1031f6dac87af28b464ecc5ce90d"; d_c0="AEBr7njMTw2PTg-BnKIjeG7KuLINqK1ENFo=|1521473500"; _xsrf=b346d3a1d11d099f8a5fd07b9b77b2d8; __utmc=51854390; __utmv=51854390.000--|2=registration_date=20180318=1^3=entry_date=20180320=1'
    #普通cookie

    topic_url = []
    topic_title = []
    tid = []
    aid = []
    artlink = []
    arttile = []
    artauthor = []

    def ua(self, uapools):
        thisua = random.choice(uapools)
        print(thisua)
        headers = ("User-Agent", thisua)
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        urllib.request.install_opener(opener)
        cookiejar = http.cookiejar.CookieJar()
        handler = urllib.request.HTTPCookieProcessor(cookiejar=cookiejar)
        opener = urllib.request.build_opener(handler, urllib.request.HTTPHandler(debuglevel=1))
        urllib.request.install_opener(opener)

    def __init__(self):
        pass

    def get_topic(self):
        '''得到话题信息'''
        self.ua(self.headers)

        firstPage = self.get_URLCode("https://www.zhihu.com/topics")

        classpat = '<li class="zm-topic-cat-item" .*?><.*?>(.*?)</a></li>'  # 话题分类
        classIDpat = '<li class="zm-topic-cat-item" data-id="(.*?)">'  # 话题分类id

        topicClass = re.compile(classpat).findall(firstPage)
        classID = re.compile(classIDpat).findall(firstPage)

        for j in range(0, len(topicClass)):

            topicurl = "https://www.zhihu.com/topics#" + urllib.parse.quote(topicClass[j])
            referurl = "https://www.zhihu.com/topics"
            topicheader = self.get_header(self.cleanCookie, referurl)
            next_page_url = 'https://www.zhihu.com/node/TopicsPlazzaListV2'

            for i in range(0, self.topicpages):
                para = {'params': '{"topic_id":' + classID[j] + ',"offset":'+ str(i*20) +',"hash_id":""}', 'method': 'next'}  # 下一页的话题参数，用offset控制。offset就是20的倍数
                realpara = urllib.parse.urlencode(para)
                topica = urllib.request.Request(url=next_page_url, headers=topicheader, data=bytes(realpara, encoding='utf-8'))
                # 通过post方法拿到下一页的数据
                topicb = urllib.request.urlopen(topica)
                topicc = topicb.read().decode("utf-8")
                sub_topics = json.loads(topicc)

                sub_topics_url = '<div class="blk">.n<a target="_blank" href="(.*?)"'
                sub_topics_id = '<div class="blk">.n<a target="_blank" href="/topic/(.*?)"'
                sub_topics_title = '<strong>(.*?)<.strong>'

                actual_topic_url = re.compile(sub_topics_url).findall(str(sub_topics))
                acutal_topic_id = re.compile(sub_topics_id).findall(str(sub_topics))
                acutal_topic_title = re.compile(sub_topics_title).findall(str(sub_topics))

                self.topic_title.append(acutal_topic_title)

                for x in acutal_topic_id:
                    self.tid.append(x)
                for y in actual_topic_url:
                    self.topic_url.append(y)

                for k in range(0, len(acutal_topic_title)):
                    topics = {"titlename":acutal_topic_title[k], "tid":acutal_topic_id[k], "class": topicClass[j]}
                    self.write_to_DB(topics, "topic")
            #测试用，请删除
            if(j==1):
                break
                break
        pass

    def get_article(self):
        '''
        @抓取话题下的文章和问答
        '''
        artile_first_url = 'https://www.zhihu.com'
        referurl2 = "https://www.zhihu.com/topics"
        art_url = 'https://www.zhihu.com/api/v4/topics/'
        topicname = self.topic_title
        toppicurl = self.topic_url
        toppicid = self.tid
        endflag = True

        if(len(self.topic_title)==0|len(self.topic_url)==0):
            print("系统未能抓取有效数据")
            pass
        else:
            for i in range(0, len(toppicurl)):

                artile_url = artile_first_url + toppicurl[i]
                artia = self.get_URLCode(artile_url)
                nextidpat = 'after_id=(.*?)&'
                nextID = re.compile(nextidpat).findall(artia)
                print(nextID)
                art_header = self.get_header(self.cleanCookie, artile_url)

                while endflag:
                    sub_data = {
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
                        "limit": "5",
                        "after_id": nextID[0]
                    }

                    realpara = urllib.parse.urlencode(sub_data)

                    art_act_url = art_url+toppicid[i]+'/feeds/top_activity?'+'/feeds/top_activity?include=data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.is_normal,comment_count,voteup_count,content,relevant_info,excerpt.author.badge[?(type=best_answerer)].topics;data[?(target.type=topic_sticky_module)].target.data[?(target.type=article)].target.content,voteup_count,comment_count,voting,author.badge[?(type=best_answerer)].topics;data[?(target.type=topic_sticky_module)].target.data[?(target.type=people)].target.answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics;data[?(target.type=answer)].target.content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[?(target.type=answer)].target.author.badge[?(type=best_answerer)].topics;data[?(target.type=article)].target.content,author.badge[?(type=best_answerer)].topics;data[?(target.type=question)].target.comment_count&limit=5&after_id=' + str(
                        nextID[0])

                    print(art_act_url)

                    art_a_url = urllib.request.Request(url=art_act_url, headers=art_header)
                    art_b_url = urllib.request.urlopen(art_a_url)
                    art_c_url = art_b_url.read().decode("utf-8","ignore")
                    art_que = json.loads(art_c_url)
                    afterpat = "'next.*?after_id=(.*?)',"
                    after = re.compile(afterpat).findall(str(art_que))

                    print(after)

                    if(after[0]=='0.00000'):
                        endflag = False
                    else:

                        authorpat = "'name': '(.*?)'"
                        linkpat = "[False|True], 'url': '(.*?)'"
                        titlepat = "'title': '(.*?)'"

                        artauthor = re.compile(authorpat).findall(str(art_que))
                        artlink = re.compile(linkpat).findall(str(art_que))
                        arttitle = re.compile(titlepat).findall(str(art_que))

                        self.artauthor=artauthor
                        self.artlink=artlink
                        self.arttile=arttitle

                        for k in range(0, len(artauthor)):
                            if (str(artauthor[k]).find('zhuanlan')) >= 0:
                                article_headers = {
                                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                                    "Content-Type": "text/html; charset=utf-8",
                                    "Cookie": self.cleanCookie,
                                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0"
                                }

                                art_url = artauthor[k].replace("http", "https")
                                artcontent = urllib.request.Request(url=art_url, headers=article_headers)

                                arti = {"title": arttitle[k], "author": artauthor[k], "aid":self.aid[k],"content": artcontent, "link": artlink[k]}

                                self.write_to_DB(arti,"topic")


                            elif ('answers' in str(artauthor[k])) == True:

                                anspat = "'" + str(artauthor[k]) + "'.*?'url':.*?'(.*?)'"
                                ans = re.compile(anspat).findall(str(art_que))

                                question = {"title": arttitle[k], "tid": self.tid[k],  "link": artlink[k]}
                                self.write_to_DB(question, "question")


                                anst = artlink[k][36:]
                                quef = ans[0][38:]

                                url_aq = 'https://www.zhihu.com/question/' + str(
                                    quef) + '/answer/' + str(anst)
                                url_aq_content = urllib.request.urlopen(url_aq).read().decode("utf-8","ignore")
                                answer = {"author": artauthor[k], "content": url_aq_content[k], "askid": anst}
                                self.write_to_DB(answer, "answer")



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
        self.conn = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="zhihu")
        if(type=="topic"):
            sql="INSERT into topic(titlename, tid, class) VALUES ("+dict["titlename"]+","+dict["tid"]+","+dict["class"]+")"
        elif(type=="article"):
            sql = "INSERT into article(title, author, aid, content, link) VALUES (" + "," + dict["title"] + "," + dict[
                "author"] + "," + dict["aid"] + "," + dict["content"] + "," + dict["link"] + ")"
        elif(type=="question"):
            sql = "INSERT into question(title, tid, link) VALUES (" + "," + dict["title"] + ","  + "," + dict["tid"] + "," +  "," + dict["link"] + ")"
        elif(type=="answer"):
            sql = "INSERT into answer(author, content, askid) VALUES (" + "," + dict["author"] + "," + dict[
                "content"] + "," + dict["askid"] + ")"
        #self.conn.commit()
        #self.conn.close()


if __name__ == '__main__':
    a = zhihuSpider()
    a.get_topic()
    a.get_article()