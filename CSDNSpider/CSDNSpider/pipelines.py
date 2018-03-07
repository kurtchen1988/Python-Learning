# -*- coding: utf-8 -*-
import urllib.request
from lxml import etree
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CsdnspiderPipeline(object):

    fileLocate = "D:\\Python\\练习\\CSDNSpider\\CSDNFile\\course\\"


    def process_item(self, item, spider):

        for i in range(0, len(item["courseName"])):
            url = item["coURL"][i]
            name = item["courseName"][i]
            data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
            treeData = etree.HTML(data)
            fullName = treeData.xpath("//div[@class='info_right no_combo no_market_price']/h1/a/text()")
            price = treeData.xpath("//span[@class='mr10']/text()")
            people = treeData.xpath("//span[@class='num']/text()")
            status = treeData.xpath("//div[@class='prog']/span[@class='lable']/text()")
            time = treeData.xpath("//span[@class='pinfo']/text()")

            try:
                fd = open(self.fileLocate+name+".txt","w",encoding="utf-8")
                if(fullName != []):
                    fd.write("课程名称: "+fullName[0]+"\n"+"课程URL: "+url+"\n"+"课程价格: "+price[0]+"\n"+"课程人数: "+people[0]+"\n"
                         +"课程状态: "+ status[0]+"\n"+"已更新课时/总课时: "+time[0])
                else:
                    fd.write("课程名称: " + name + "\n" + "课程URL: " + url + "\n" + "课程价格: " + price[0] + "\n" + "课程人数: " +
                             people[0] + "\n"+ "课程状态: " + status[0] + "\n" + "已更新课时/总课时: " + time[0])
                fd.close()
            except Exception as err:
                print(err)

        return item
