'''
@
@知乎话题广场爬虫程序
@
@   第一步：获取广场所有主话题和其编号
@   第二步：基于编号和主话题构建并爬取每一个主话题的所有子话题
@   第三部：基于子话题编号等信息爬取该话题下文章和问答
@
@   这里主要实现了Hot Tab[讨论]下的内容，至于索引[index]\精华[top-answers]\等待回答[unanswered]构造原理类似
@       => 比如：精华，通过limit和offset的同步变化来实现滚动获取更多内容，limite=20&offset=20
@
@实际使用中，潜在的问题就是验证码的出现，需要同步使用浏览器伪装池和IP代理池技术，IP代理池需要使用高质量收费的代理
@
@在对文章和问答所需信息结对分析后，发现有些时候抓取的信息存在问题，所需信息间不是对等出现，问题不是爬虫本身的问题，只要存在信息不配对出现的情况，对应的5条信息就做舍去处理
@
'''
# -*- coding: utf-8 -*-
import urllib.request
import pymysql
import time, re, os
import requests
import random
import urllib.parse
import http.cookiejar
import ssl
import json
from lxml import etree

'''
@定义User-Agent Pool
@后续计划：这里从一个包含超过100条User-Agent记录的Txt文件中读取，这样UA的范围会更大
'''
uapools = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.3",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0",
    "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1"
]

# 设置数据库连接
conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", db="zhihu", use_unicode=True,
                       charset="utf8")


# 定义User-Agent
def ua(uapools):
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
    return thisua


# 数据库操作函数
def sql_opr(sql):
    conn.query(sql)
    conn.commit()


'''
@知乎话题广场爬虫程序
@逐层通过分析话题 - 子话题，进而获取文章和问答Url - 文章和问答内容
'''


def zhihu_topics():
    # 设置User-Agent和SSL
    ua(uapools)
    ssl._create_default_https_context = ssl._create_unverified_context

    # 话题广场入口
    topics_url = ['https://www.zhihu.com/topics']

    '''
    @开启信息抓取操作和异常捕捉
    '''
    try:
        # 获取话题广场的内容
        topicsdata = urllib.request.urlopen(topics_url[0]).read().decode("utf-8", "ignore")
        patid = 'class="zm-topic-cat-item" data-id="(.*?)"'
        patkw = 'class="zm-topic-cat-item" data-id=".*?"><a href="(.*?)"'

        # 获取全部Topics和ID
        rstid = re.compile(patid, re.S).findall(topicsdata)
        rstkw = re.compile(patkw, re.S).findall(topicsdata)

        print("知乎话题广场，共包含：[" + str(len(rstkw)) + "]个主话题")

        '''
        @抓取知乎广场所有话题的程序
        @这里为了测试功能，直接设定了循环区间
        '''
        for topic_i in range(0, 2):
            # for topic_i in range(0, len(rstkw)):
            print(
                str(topic_i + 1) + " => 开始处理第<" + str(topic_i + 1) + ">个子话题 - " + urllib.parse.unquote(rstkw[topic_i]))
            # 构造第一个Topic的第一个链接并获取信息
            topic_url = topics_url[0] + urllib.parse.unquote(rstkw[topic_i])
            print("     Url： " + str(topic_url))

            '''
            @用XPath获取知乎广场所有话题和ID
            #topic_data = urllib.request.urlopen(topic_url).read().decode("utf-8", "ignore")
            #topic_data_format = etree.HTML(topic_data)
            #links = topic_data_format.xpath('//div[@class="blk"]/a[@target="_blank"]/@href')
            #kw = topic_data_format.xpath('//div[@class="blk"]/a/strong/text()')
            '''

            '''
            @抓取子话题的程序
            '''
            sub_topic_i = 0
            # 子Topic Url_入口Url
            sub_topic_url = 'https://www.zhihu.com/node/TopicsPlazzaListV2'
            sub_continue = True
            while sub_continue:

                '''
                @抓包分析获得参数
                @method:next
                @params:{"topic_id":253,"offset":20,"hash_id":""}
                '''
                # 构造和格式化参数
                data = {
                    'method': 'next',
                    'params': '{"topic_id":' + rstid[topic_i] + ',"offset":' + str(
                        (sub_topic_i) * 20) + ',"hash_id":""}'
                }
                params = urllib.parse.urlencode(data)

                # 构造Headers
                headers = {
                    "Accept": "*/*",
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

                try:
                    # 获取子话题内容并格式化
                    requests.packages.urllib3.disable_warnings()
                    sub_topic_url_info = requests.post(sub_topic_url, params=params, headers=headers, verify=False)
                    sub_topics_info = json.loads(sub_topic_url_info.text)

                    # 数据式样：<div class="item"><div class="blk">\n<a target="_blank" href="/topic/19646175">
                    psub_topics_url = '<div class="blk">.n<a target="_blank" href="(.*?)"'
                    psub_topics_title = '<strong>(.*?)<.strong>'

                    '''
                    @第一步：获取子话题编号和标题
                    @第二步：写入数据
                    @第三部：获取文章和问答信息并写入数据库
                    '''
                    rsub_topics_url = re.compile(psub_topics_url, re.S).findall(str(sub_topics_info))
                    rsub_topics_title = re.compile(psub_topics_title, re.S).findall(str(sub_topics_info))

                    # 数据写入输数据库
                    for topic_db in range(0, len(rsub_topics_url)):
                        tid = rsub_topics_url[topic_db]
                        tname = rsub_topics_title[topic_db]
                        topic = rstkw[topic_i]
                        comments = ' '
                        sql = "insert into topics(tid, tname, topic, comments) values('" + tid + "', '" + tname + "', '" + topic + "', '" + comments + "')"
                        sql_opr(sql)

                    sub_topic_i += 1

                    # 如果结果中长度为0，意味着已经滚动到最后一页
                    if len(rsub_topics_title) == 0:
                        sub_continue = False
                    else:
                        '''
                        @抓取子话题下的文章和问答
                        '''
                        sub_url_url1 = ['https://www.zhihu.com']
                        for sub_content_i in range(0, len(rsub_topics_title)):
                            # 构造子话题Url
                            sub_url_url2 = sub_url_url1[0] + str(rsub_topics_url[sub_content_i])
                            print("        子话题连接为: " + str(sub_url_url2))
                            sub_url_url2 = sub_url_url2 + '/hot'
                            '''
                            @从子话题的默认页的源码中获取第一页的入口参数，这是获取其它参数的基础
                            '''
                            entrydata = urllib.request.urlopen(sub_url_url2).read().decode('utf-8', 'ignore')
                            pentrydata = 'after_id=(.*?)&'
                            rentrydata = re.compile(pentrydata, re.S).findall(entrydata)
                            print("          (001) - " + str(rentrydata))

                            # 构造Headers
                            sub_content_headers = {
                                "authorization": "oauth c3cef7c66a1843f8b3a9e6a1e3160e20",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0"
                            }

                            sub_url_continue = True
                            cycle = 2
                            while sub_url_continue:
                                # 构造参数
                                sub_data = {
                                    "limit": "5",
                                    "after_id": str(rentrydata)
                                }
                                sub_params = urllib.parse.urlencode(sub_data)

                                requests.packages.urllib3.disable_warnings()
                                # 构造文章和问答信息链接Url
                                url_url = 'https://www.zhihu.com/api/v4/topics/' + str(rsub_topics_url[sub_content_i])[
                                                                                   7:] + '/feeds/top_activity?include=data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.is_normal,comment_count,voteup_count,content,relevant_info,excerpt.author.badge[?(type=best_answerer)].topics;data[?(target.type=topic_sticky_module)].target.data[?(target.type=article)].target.content,voteup_count,comment_count,voting,author.badge[?(type=best_answerer)].topics;data[?(target.type=topic_sticky_module)].target.data[?(target.type=people)].target.answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics;data[?(target.type=answer)].target.content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[?(target.type=answer)].target.author.badge[?(type=best_answerer)].topics;data[?(target.type=article)].target.content,author.badge[?(type=best_answerer)].topics;data[?(target.type=question)].target.comment_count&limit=5&after_id=' + str(
                                    rentrydata[0])
                                # 获取文章和问答信息，其中：
                                #   第一页的信息--在首页源码里，格式 => after_id=4478.31547 => 通过这页的信息可以获取下一页的ID: 4477.11153
                                sub_topic_url_url_info = requests.get(url_url, headers=sub_content_headers,
                                                                      verify=False)
                                # 数据格式化
                                sub_topics_url_url_info = json.loads(sub_topic_url_url_info.text)
                                purl_url = "'next.*?after_id=(.*?)',"
                                rurl_url = re.compile(purl_url, re.S).findall(str(sub_topics_url_url_info))
                                rentrydata = rurl_url

                                # 设定所有编号都为3位数
                                if cycle < 10:
                                    str_cycle = '00' + str(cycle)
                                elif cycle >= 10 and cycle < 100:
                                    str_cycle = '0' + str(cycle)
                                else:
                                    str_cycle = str(cycle)

                                print("          (" + str_cycle + ") - " + str(rentrydata))
                                cycle += 1

                                # 如果获取的结果为0.00000，说明内容已经滚动到最后一页
                                if rurl_url[0] == '0.00000':
                                    sub_url_continue = False
                                    cycle = 2
                                else:
                                    # 抓取文章和问答信息
                                    pname = "'name': '(.*?)'"
                                    # aq = article & question
                                    # paq = "False}, 'url':.*?'(.*?)'" or "True}, 'url':.*?'(.*?)'"
                                    paq = "[False|True]}, 'url':.*?'(.*?)'"
                                    ptitle = "'title': '(.*?)'"
                                    rname = re.compile(pname, re.S).findall(str(sub_topics_url_url_info))
                                    raq = re.compile(paq, re.S).findall(str(sub_topics_url_url_info))
                                    rtitle = re.compile(ptitle, re.S).findall(str(sub_topics_url_url_info))
                                    # print(str(sub_topics_url_url_info))
                                    # print(rname, raq, rtitle)
                                    # print(len(rname))
                                    # print(len(raq))
                                    # print(len(rtitle))

                                    # 如果爬取的内容非对称出现，经过分析是，页面信息有问题，这样的信息直接舍弃
                                    if (len(raq) != 5 or len(rtitle) != 5):
                                        # 直接舍弃掉
                                        pass
                                    else:
                                        # 分门别类处理相关信息
                                        # 文章直接处理
                                        # 如果是Answer，获取其Question信息[Link等]
                                        # 数据写入数据库
                                        for aq_i in range(0, len(rname)):
                                            # 获取Topic编号信息
                                            cursor = conn.cursor()
                                            # 之所以取最大的，是因为数据库中存在一些测试数据，最大的记录为最新数据
                                            sql_tid = "SELECT MAX(id) FROM topics where tname = '" + rsub_topics_title[
                                                sub_content_i] + "' LIMIT 1"
                                            cursor.execute(sql_tid)
                                            s_tid = cursor.fetchall()
                                            conn.commit()
                                            s_tid = re.sub("\D", "", str(s_tid[0]))
                                            if (str(raq[aq_i]).find('zhuanlan')) >= 0:
                                                # print("--Zhuanlan--")
                                                # 信息插入Article表格
                                                sql_article = "insert into article(title, link, tid) values('" + rtitle[
                                                    aq_i] + "', '" + raq[aq_i] + "', '" + s_tid + "')"
                                                sql_opr(sql_article)

                                                # 获取Article Id编号信息
                                                cursor = conn.cursor()
                                                # print("------" + str(raq[aq_i]))
                                                sql_aid = "SELECT MAX(id) FROM article where link = '" + raq[
                                                    aq_i] + "' LIMIT 1"
                                                cursor.execute(sql_aid)
                                                s_aid = cursor.fetchall()
                                                conn.commit()
                                                s_tid = re.sub("\D", "", str(s_aid[0]))
                                                # print(s_tid)

                                                # 获取Article信息并插入Articles表格中
                                                # 之所以取最大的，是因为数据库中存在一些测试数据，最大的记录为最新数据
                                                # racontent = urllib.request.urlopen(raq[aq_i]).read().decode("utf-8","ignore")
                                                # print(racontent)
                                                # print(raq[aq_i])
                                                # print(aq_i)

                                                # 构造Headers - 这里不用Headers也没啥影响
                                                article_content_headers = {
                                                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                                                    "Content-Type": "text/html; charset=utf-8",
                                                    "Cookie": 'q_c1=2f36189ed07842fea5d63abcf6dcfe6c|1521378566000|1521378566000; capsion_ticket="2|1:0|10:1521647439|14:capsion_ticket|44:MTIxYjY2MzMwNTY0NDczOTg3MDA2NmFmOGE1YTEyMzA=|704aa26d53a212ac3e1cb94daa76f9a3b3859915efd3f33168ceba572abff649"; _zap=34f289cd-73fc-4362-a6fa-5c39b0c71f35; r_cap_id="MmZmZjY1NTc0YzcxNGY3N2JmNmU5MTI1NGQwMzc5ZTU=|1521984642|752d9c90b0e5d5899bbcb87e736a7bfdffb79ba6"; cap_id="MGFiYjIzNDQ4MzcxNDFiY2IxNzk3NDhkMTRmYjBhOTc=|1521984642|8d3f44f3657890ac9d4b9da35e5e94cbf2d4bccd"; __utma=51854390.1682481854.1521854909.1521854909.1521854909.1; __utmz=51854390.1521816109.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); l_cap_id="ODg2ZDIxZjcxMjM2NDQ5M2IwZGE4Mjc5MGQ2YTlhOGU=|1521984642|9640e26aadddc5ed99bbffa0d462c140f8075153"; d_c0="AEBr7njMTw2PTg-BnKIjeG7KuLINqK1ENFo=|1521473500"; __DAYU_PP=YaIZ2qqNnFaUjmrM2mJE2ae176e06890; XSRF-TOKEN=2|4d339df3|3870283fb4a290fdcbe76b79ebbca30b|1521894620',
                                                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0"
                                                }

                                                raq_str = raq[aq_i].replace("http", "https")
                                                # racontent = urllib.request.urlopen(raq[aq_i]).read().decode("utf-8","ignore")
                                                racontent = requests.get(raq_str, headers=article_content_headers,
                                                                         verify=False)
                                                # 数据格式化
                                                # racontent = json.loads(racontent.text)
                                                str_racontent = racontent.text.replace("'", "\\'")
                                                cursor = conn.cursor()
                                                # sql_articles = "insert into articles(author, content, aid) values('"+rname[aq_i]+"', '"+ str_racontent[:10000] +"', '"+s_tid+"')"
                                                # print(raq_str)
                                                sql_articles = "insert into articles(author, content, aid) values('" + \
                                                               rname[
                                                                   aq_i] + "', '" + str_racontent + "', '" + s_tid + "')"
                                                sql_opr(sql_articles)


                                            elif ('answers' in str(raq[aq_i])) == True:
                                                pq = "'" + str(raq[aq_i]) + "'.*?'url':.*?'(.*?)'"
                                                # print(pq)
                                                rq = re.compile(pq, re.S).findall(str(sub_topics_url_url_info))
                                                # print(raq[aq_i],rq)
                                                # 信息插入Ask表格
                                                sql_ask = "insert into ask(title, link, question, tid) values('" + \
                                                          rtitle[aq_i] + "', '" + raq[aq_i] + "', '" + rq[
                                                              0] + "', '" + s_tid + "')"
                                                sql_opr(sql_ask)

                                                # 爬取回答信息
                                                # 示例Url: https://www.zhihu.com/question/269416619/answer/350316694
                                                aaid = raq[aq_i][36:]
                                                qqid = rq[0][38:]
                                                # print(aaid, qqid)
                                                # 构建Url
                                                url_aq = 'https://www.zhihu.com/question/' + str(
                                                    qqid) + '/answer/' + str(aaid)
                                                url_aq_content = urllib.request.urlopen(url_aq).read().decode("utf-8",
                                                                                                              "ignore")
                                                str_aq = url_aq_content.replace("'", "\\'")
                                                cursor = conn.cursor()

                                                sql_answer = "insert into answer(author, content, aid) values('" + \
                                                             rname[aq_i] + "', '" + str_aq + "', '" + url_aq + "')"
                                                sql_opr(sql_answer)

                                            else:
                                                # print("--Not Execution--")
                                                pass
                except Exception as Err1:
                    print(Err1)
        # 关闭数据库连接
        conn.close()
    except Exception as Err:
        print(Err)


zhihu_topics()
