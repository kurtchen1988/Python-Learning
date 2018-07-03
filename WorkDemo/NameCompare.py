import pymysql
import time


class ComName:

    sqlsupplier ="select supplier_id, name from db_supplier.supplier_baseinfo where audit_status = 'DONE' and last_operationtime<'%s' and last_operationtime>'%s' order by supplier_id;"
    sqlshop ="select id, outer_id, name from db_item.parana_shops where outer_id in (%s) order by outer_id;" # db_supplier.supplier_baseinfo.supplier_id
    sqlshopCom ="select id, outer_id, name from db_item.parana_shops where outer_id in (%s) and name !='%s' order by id"
    sqlUpdate = "update db_item.parana_shops set name = '%s' where id = '%s' and outter_id = '%s';"
    sqlItemUpdate = "update db_item.parana_items set shop_name='%s' WHERE shop_id= %s;"
    # update db_item.parana_shops set name = '%s' where id ='%s' and name = '%s'

    user = 'devread'
    passwd = 'devR3343'
    urlprod = 'rr-9dpnbsn9mds4urq9g.mysql.rds.aliyuncs.com'
    urlitems = 'rr-9dp30iap52gda17cz.mysql.rds.aliyuncs.com'



    allSupplier = None
    allShop = None

    shopSQL = []
    difference = []
    same = []
    finaldata = []


    def __init__(self):
        self.dbprd = pymysql.connect(host=self.urlprod, user=self.user, password=self.passwd, port=3306, charset='utf8')  # production数据库
        self.dbitem = pymysql.connect(host=self.urlitems, user=self.user, password=self.passwd, port=3306, charset='utf8')  # item数据库

        self.curprd = self.dbprd.cursor()
        self.curitem = self.dbitem.cursor()

    def getNowTime(self, NowFlag):
        if(NowFlag==None):
            nowTime = time.strftime("%Y-%m-%d", time.localtime())
        else:
            nowTime=NowFlag

        return nowTime

    def getPassTime(self, Month):
        if(Month==None):
            passTime = time.strftime("%Y", time.localtime()) +'-'+ str(int(time.strftime("%m", time.localtime()))-1) +'-'+ time.strftime("%d", time.localtime())
        else:
            passTime = Month
        return passTime

    def getSupplier(self,NowFlag, Month):

        self.curprd.execute(self.sqlsupplier%(self.getNowTime(NowFlag),self.getPassTime(Month)))
        self.allSupplier = self.curprd.fetchall()

        for sup in range(0, len(self.allSupplier)):
            if sup == len(self.allSupplier) -1:
                self.shopSQL.append(str(self.allSupplier[sup][0]))
            else:
                self.shopSQL.append(str(self.allSupplier[sup][0])+', ')

        return self.sqlshop % (''.join(self.shopSQL))

    def getShop(self,ShopSQL):
        #print(ShopSQL)
        self.curitem.execute(ShopSQL)
        self.allShop = self.curitem.fetchall()
        print("供应商表(db_supplier.supplier_baseinfo)中共有："+str(len(self.allSupplier))+" 条数据")
        print("店铺表(db_item.parana_shops)中共有："+str(len(self.allShop))+" 条数据")
        #print(self.allSupplier)
        #print(self.allShop)
        self.getDif(self.allShop, self.allSupplier)

        return self.allShop

    def getDif(self, shop, supplier):

        if len(supplier) > len(shop):
            print("供应商表(db_supplier.supplier_baseinfo)比店铺表(db_item.parana_shops)中数据更多，数据处理中...")
            for a in supplier:
                m = 0
                for i in shop:
                    m=m+1
                    if str(a[0])==str(i[1]):
                        self.same.append(a)
                        break;
                    elif str(a[0])!=str(i[1]) and m == len(shop):
                        self.difference.append(a)

        elif len(supplier) < len(shop):
            print("店铺表(db_item.parana_shops)比供应商表(db_supplier.supplier_baseinfo)中数据更多，程序将按照店铺表数据为基准生成，请查看原因。数据处理中...")
            for a in shop:
                m = 0
                for i in supplier:
                    m=m+1
                    if str(a[1])==str(i[0]):
                        self.same.append(i)
                        break;
                    elif str(a[1])!=str(i[0]) and m == len(supplier):
                        self.difference.append(i)
        else:
            print("店铺表(db_item.parana_shops)和供应商表(db_supplier.supplier_baseinfo)数据相同 ")

    def getCom(self):
        print("调整主数据为："+str(len(self.same))+" 条数据")
        print("店铺数据为："+str(len(self.allShop))+" 条数据")

        #print(self.same)
        #print(self.allShop)

        for a in self.same:
            m=0
            for b in self.allShop:
                m=m+1
                if str(a[1])== str(b[2]) and str(a[0]) == str(b[1]):
                    break
                elif str(a[1])!=str(b[2]) and m==len(self.allShop):
                    self.curitem.execute(self.sqlshop%(str(a[0])))
                    res = self.curitem.fetchall()
                    self.finaldata.append([res[0][0],a[0],a[1]])

        return self.finaldata


    def genSQL(self, finalData):
        print("生成更新语句中...")
        file = open('./nameUpdate.sql','w+',encoding='gbk')

        file.write('-- 店铺更新语句\n')
        for a in finalData:
            # sqlUpdate = "update db_item.parana_shops set name = '%s' where id ='%s' and outter_id = '%s'"

            file.write(self.sqlUpdate%(a[2],a[0],a[1])+'\n')

        file.write('-- 商品更新语句\n')
        for c in finalData:

            file.write(self.sqlItemUpdate%(c[2],c[0])+'\n')

        file.write("-- 回滚语句\n")

        file.write('-- 店铺回滚语句\n')
        for b in finalData:
            self.curitem.execute(self.sqlshop%(b[1]))
            res = self.curitem.fetchall()

            file.write(self.sqlUpdate%(res[0][2],a[0],a[1])+'\n')

        file.write('-- 商品回滚语句\n')
        for d in finalData:
            self.curitem.execute(self.sqlshop % (d[1]))
            res = self.curitem.fetchall()

            file.write(self.sqlItemUpdate % (res[0][2], d[0])+'\n')

        file.close()
        print("SQL文件生成成功（nameUpdate.sql），请在本文件的相同位置查看！")

    def __del__(self):
        self.curitem.close()
        self.curprd.close()
        self.dbprd.close()
        self.dbitem.close()

if __name__ == '__main__':

    a = ComName()
    date = input("请输入查询的结束时间(以2018-06-01这种格式来输入，如果是当日请直接回车)：")
    month = input("请输入查询的开始时间(以2018-06-01这种格式来输入，如果是一个月前请直接回车)：")
    if date=='':
        if month == '':
            a.getShop(a.getSupplier(None, None))
            a.genSQL(a.getCom())
        else:
            a.getShop(a.getSupplier(None,month))
            a.genSQL(a.getCom())
    else:
        if month == '':
            a.getShop(a.getSupplier(date, None))
            a.genSQL(a.getCom())
        else:
            a.getShop(a.getSupplier(date, month))
            a.genSQL(a.getCom())
    #a.genSQL()

