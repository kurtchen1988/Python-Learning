import pymysql


class ComID:

    sqltrade ="SELECT id FROM db_trade.zcy_orders where created_at between '2018-05-24' and '2018-07-24' and status in (0, 1) and order_type=0"
    sqlitem ="SELECT distinct(order_id) FROM db_item.zcy_sku_warehouses where create_at between '2018-05-24' and '2018-07-24'"

    
    # update db_item.parana_shops set name = '%s' where id ='%s' and name = '%s'

    user = 'devread'
    passwd = 'devR3343'
    urlprod = 'rr-9dpnbsn9mds4urq9g.mysql.rds.aliyuncs.com'
    urlitems = 'rr-9dp30iap52gda17cz.mysql.rds.aliyuncs.com'



    allTrade = None
    allItem = None

    tradeID = []
    itemID = []
    dif = []


    def __init__(self):
        self.dbtrade = pymysql.connect(host=self.urlprod, user=self.user, password=self.passwd, port=3306, charset='utf8')
        self.dbitem = pymysql.connect(host=self.urlitems, user=self.user, password=self.passwd, port=3306, charset='utf8')

        self.curtrade = self.dbtrade.cursor()
        self.curitem = self.dbitem.cursor()



    def getDate(self):

        self.curtrade.execute(self.sqltrade)
        self.allTrade = self.curtrade.fetchall()

        self.curitem.execute(self.sqlitem)
        self.allItem = self.curitem.fetchall()

        for tra in self.allTrade:
            self.tradeID.append(tra[0])

        for ite in self.allItem:
            self.itemID.append(ite[0])

        for a in self.tradeID:
            if a not in self.itemID:
                self.dif.append(a)
            elif a in self.itemID:
                pass

        file = open('./orderID.txt', 'w+', encoding='gbk')
        file.write(str(self.dif))

    def __del__(self):

        self.curtrade.close()
        self.curitem.close()

if __name__ == '__main__':

    a = ComID()
    a.getDate()

