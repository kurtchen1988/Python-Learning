import pymysql
import requests

class sqlInser():

    sql2 = "SELECT org_id, dist_id, name, short_name, org_code,budget_org_code FROM db_user.vanyar_purchase_institution WHERE budget_org_code IS NOT NULL and status =1 and budget_org_code !='' and dist_id ='339900'"  # 采购单位
    sql3 = "SELECT parent_code ,code FROM db_metadata.dc_platform_codeset_item WHERE codeset_id ='6';" # 1 预算科目
    sql4 = "SELECT parent_code ,code FROM db_metadata.dc_platform_codeset_item WHERE codeset_id ='5';" # 2 经济科目
    sql5 = "SELECT node_id,parent_node_id,code, level, name  FROM db_manage.zcy_gpcatalog_node_t WHERE gp_catalog_id ='1000000000000010450' and is_deprecated ='0';" # 采购目录


    urlsup = 'http://10.110.2.31:8080/technical/institution/add'
    urlcat = 'http://10.110.2.31:8080/technical/subject/add'
    urlbuget = 'http://10.110.2.31:8080/technical/gpcatlog/add'

    user = 'devread'
    passwd = 'devR3343'
    urlmeta = 'rm-9dp1quffelmxt4b12.mysql.rds.aliyuncs.com'
    urluser = 'rm-9dpgi2299i21zn82e.mysql.rds.aliyuncs.com'
    urlmanage = 'rm-9dpv13x7hy6juegta.mysql.rds.aliyuncs.com'


    def __init__(self):
        self.dbmeta = pymysql.connect(host=self.urlmeta, user=self.user, password=self.passwd, port=3306, charset='utf8')  # meta数据库
        self.dbuser = pymysql.connect(host=self.urluser, user=self.user, password=self.passwd, port=3306, charset='utf8')  # user数据库
        self.dbmanage = pymysql.connect(host=self.urlmanage, user=self.user, password=self.passwd, port=3306, charset='utf8')  # manage数据库

        self.curmeta = self.dbmeta.cursor()
        self.curuser = self.dbuser.cursor()
        self.curmanage = self.dbmanage.cursor()

    def setSup(self, orgid, distid, name, short_name, org_code, budget_code):
        supdata = {'orgid': orgid,
                   'distid': distid,
                   'name': name,
                   'short_name': short_name,
                   'org_code': org_code,
                   'budget_code': budget_code,
                   'status': 10,
                   }
        return supdata

    def setCat(self, partner, code, name, type):
        catdata = {'partner': partner,
                   'code': code,
                   'name': name,
                   'type': type,
                   }
        return catdata

    def setBuget(self, node,partner, code, level, name):

        bugetdata = {'node': node,
                     'partner': partner,
                     'code': code,
                     'level': level,
                     'name': name,
                     }
        return bugetdata

    def postData(self, url, data):
        return requests.post(url=url,data=data)

    def getData(self, cursor, sql):
        cursor.execute(sql)
        return cursor.fetchall()

    def mainControl(self):

        # 采购单位
        danwei = self.getData(self.curuser,self.sql2)
        for i in danwei:
            data = self.setSup(orgid=i[0],distid=i[1],name=i[2],short_name=i[3],org_code=i[4],budget_code=i[5])
            self.postData(url=self.urlsup, data=data)

        # 经济和预算1 n
        yusuan1 = self.getData(self.curmeta,self.sql3)
        for n in yusuan1:
            data = self.setCat(partner=n[0],code=n[1],name=n[2],type=1)
            self.postData(url=self.urlbuget, data=data)

        # 经济和预算2 m
        yusuan2 = self.getData(self.curmeta, self.sql4)
        for m in yusuan2:
            data = self.setCat(partner=m[0], code=m[1],name=m[2],type=2)
            self.postData(url=self.urlbuget, data=data)

        # 采购目录 x
        caigou = self.getData(self.curmanage, self.sql5)
        for x in caigou:
            data = self.setBuget(node=x[0], partner=x[1], code=x[2], level=x[3], name=x[4])
            self.postData(url=self.urlcat, data=data)

    def __del__(self):


        self.curmeta.close()
        self.curuser.close()
        self.curmanage.close()

        self.dbmeta.close()
        self.dbuser.close()
        self.dbmanage.close()



if __name__ == '__main__':
    a = sqlInser()
    a.mainControl()