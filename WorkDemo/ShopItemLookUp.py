import pymysql


sqlshop = 'select id from db_item.parana_shops where id = %s'
sqlitem = 'select * from db_item.parana_items where shop_id = %s'
sqlsupplier = 'select supplier_id from db_supplier.supplier_baseinfo where name like (%%s%)'

user = 'devread'
passwd = 'devR3343'
urlprod = 'rr-9dpnbsn9mds4urq9g.mysql.rds.aliyuncs.com'
urlitems = 'rr-9dp30iap52gda17cz.mysql.rds.aliyuncs.com'

def __init__():
    dbprd = pymysql.connect(host=urlprod, user=user, password=passwd, port=3306, charset='utf8')
    dbitem = pymysql.connect(host=urlitems, user=user, password=passwd, port=3306, charset='utf8')

    curprd = dbprd.cursor()
    curitem = dbitem.cursor()

def showAll(shopName):
    pass