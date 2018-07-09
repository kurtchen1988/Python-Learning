import pymysql
import time

class attriSQL:

    user = 'devread'
    passwd = 'devR3343'
    urlprod = 'rr-9dpnbsn9mds4urq9g.mysql.rds.aliyuncs.com'
    urlitems = 'rr-9dp30iap52gda17cz.mysql.rds.aliyuncs.com'

    sqlItem = "SELECT id, attrs_json from db_item.parana_skus WHERE id in(%s) and attrs_json is not null;"
    sqlProd = "SELECT  sku_id from db_trade.zcy_order_items WHERE created_at BETWEEN '2018-07-04 00:00:00' and  '2018-07-04 12:00:00' and attribute is null;"

    skuid = []
    itemList = {}

    def __init__(self):
        self.dbItem = pymysql.connect(host=self.urlitems, user=self.user, password=self.passwd, port=3306, charset='utf8')
        self.dbProd = pymysql.connect(host=self.urlprod, user=self.user, password=self.passwd, port=3306, charset='utf8')
        self.curItem = self.dbItem.cursor()
        self.curProd = self.dbProd.cursor()

    def getSkuid(self):
        self.curProd.execute(self.sqlProd)
        sku = self.curProd.fetchall()
        for id in sku:
            self.skuid.append(id[0])
        print(self.skuid)

    def getItem(self):
        for sql in self.skuid:
            self.curItem.execute(self.sqlItem%sql)
            item = self.curItem.fetchall()
            #print(item)
            if item == () or item[0][1] == '[]':
                # print(sql)
                pass
            else:
                #print(item)
                a = [item[0][0],item[0][1]]
                self.itemList.append(a)
            print(self.itemList)
        print(self.itemList)

    def __del__(self):
        self.dbProd.close()
        self.dbItem.close()
        self.curItem.close()
        self.curProd.close()

if __name__=='__main__':
    a = attriSQL()
    a.getSkuid()
    a.getItem()
