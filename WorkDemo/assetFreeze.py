import pymysql


class freeze:

    freeze1 = "update db_item.zcy_item_district_relation set status=-2 where item_id = %s and sign_distrcit_code=%s;"
    freeze2 = "update db_item.parana_items set status=-2 where id = %s and sign_distrcit_code=%s;"
    freeze3 = "INSERT INTO `db_item`.`zcy_item_audit_log` (`item_id`, `item_audit_id`, `original_status`, `new_status`, `audit_result`, `audit_comment`, `creator_id`, `created_at`, `creator_name`, `creator_org`, `type`, `creator_org_id`) VALUES (%s, null, 'UNDERSHELF', 'FROZEN', 'FREEZE', '非招标商品（药品）', 1000169897, now(), '运维平台', '运营机构', '0', 1);"

    freezeUn1 = "update db_item.zcy_item_district_relation set status=%s where item_id = %s and sign_district_code=%s;"
    freezeUn2 = "update db_item.parana_items set status=%s where id = %s and sign_district_code=%s;"
    freezeUn3 = "delete from `db_item`.`zcy_item_audit_log` where item_id = %s;"

    freezeAll1 = "update db_item.parana_items set status=-2 where id = %s;"
    freezeAll2 = "update db_item.zcy_item_district_relation set status=-2 where id = %s;"
    freezeAll3 = "INSERT INTO `db_item`.`zcy_item_audit_log` (`item_id`, `item_audit_id`, `original_status`, `new_status`, `audit_result`, `audit_comment`, `creator_id`, `created_at`, `creator_name`, `creator_org`, `type`, `creator_org_id`) VALUES (%s, null, 'UNDERSHELF', 'FROZEN', 'FREEZE', '非招标商品（药品）', 1000169897, now(), '运维平台', '运营机构', '0', 1);"

    freezeAllUn1 = "update db_item.parana_items set status=%s where id = %s;"
    freezeAllUn2 = "update db_item.zcy_item_district_relation set status=%s where item_id = %s;"
    freezeAllUn3 = "delete from `db_item`.`zcy_item_audit_log` where item_id = %s;"

    itemQuery = "select count(*) from db_item.zcy_item_district_relation where item_id = %s;"
    itemQuery2 = "select sign_district_code from db_item.zcy_item_district_relation where item_id = %s;"
    itemQuery3 = "select status from db_item.zcy_item_district_relation where item_id = %s;"
    itemQuery4 = "select status from db_item.parana_items where id = %s;"
    user = 'devread'
    passwd = 'devR3343'
    urlitems = 'rr-9dp30iap52gda17cz.mysql.rds.aliyuncs.com'
    item_id = []
    district_id = []
    finalUpSql = []
    finalReSql = []

    def __init__(self):
        self.dbitem = pymysql.connect(host=self.urlitems, user=self.user, password=self.passwd, port=3306,
                                      charset='utf8')  # item数据库
        self.curitem = self.dbitem.cursor()

    def setSQL(self, item_id, district_id):
        return {'one':self.freeze1%(item_id, district_id),'two':self.freeze2%(item_id, district_id),'three':self.freeze3%(item_id)}

    def setItems(self, itemId):
        return self.item_id.append(itemId)

    def queryData(self, sql):
        self.curitem.execute(sql)
        return self.curitem.fetchall()

    def getNum(self, itemId):
        return self.queryData(self.itemQuery%(itemId))

    def getDistrict(self, itemId):
        return self.queryData(self.itemQuery2%(itemId))

    def getStatus(self, itemId):
        return  self.queryData(self.itemQuery3%(itemId))

    def getItemStatus(self, itemId):
        return  self.queryData(self.itemQuery4%(itemId))

    def mainFlow(self):
        while True:
            item = input("请输入逐个商品ID并回车，若结束请按q键并回车：")

            if item == "q":
                break
            else:
                self.item_id.append(item)
        print("共输入"+str(len(self.item_id))+"个商品ID...")
        flag = input("输入1把商品全网冻结，0为逐个商品某个区划内冻结")

        if flag == '1':
            for m in self.item_id:
                if self.getStatus(m)[0][0]==-3:
                    pass
                else:
                    self.finalUpSql.append(self.freezeAll1%(m))
                    self.finalUpSql.append(self.freezeAll2%(m))
                    self.finalUpSql.append(self.freezeAll3%(m))

                    self.finalReSql.append(self.freezeAllUn1%(self.getStatus(m)[0][0], m))
                    self.finalReSql.append(self.freezeAllUn2%(self.getStatus(m)[0][0], m))
                    self.finalReSql.append(self.freezeAllUn3%(m))
        elif flag == '0':
            for i in self.item_id:
                numDis = self.getNum(i)[0][0]
                if (self.getStatus(i)[0][0] !=-3):
                    if(numDis!=None and numDis!=1):
                        print("查询到商品"+i+"有以下的区划：")
                        print(self.getDistrict(i))
                        while True:
                            district = input("请逐个输入商品"+i+"需要取消的区划并回车，若结束请按q键并回车：")
                            if district == "q":
                                if(len(self.district_id)!=0):
                                    self.finalUpSql.append(self.freeze3 % (i))
                                    self.finalReSql.append(self.freezeUn3 % (i))
                                    for x in self.district_id:
                                        self.finalUpSql.append(self.freeze1%(i,x))
                                        self.finalUpSql.append(self.freeze2%(i,x))


                                        self.finalReSql.append(self.freezeUn1%(self.getStatus(i)[0][0],i,self.getDistrict(i)[0][0]))
                                        self.finalReSql.append(self.freezeUn2%(self.getItemStatus(i)[0][0],i,self.getDistrict(i)[0][0]))

                                    break
                                else:
                                    print("区划有问题了！")
                                    break
                            else:
                                self.district_id.append(district)
                    elif (numDis!=None and numDis==1):
                        print("查询到商品" + i + "只有一个区划："+self.getDistrict(i)[0][0]+"。 已将此商品加入队列。")
                        self.finalUpSql.append(self.freeze1%(i,self.getDistrict(i)[0][0]))
                        self.finalUpSql.append(self.freeze2%(i,self.getDistrict(i)[0][0]))
                        self.finalUpSql.append(self.freeze3%(i))

                        self.finalReSql.append(self.freezeUn1%(self.getStatus(i)[0][0], i, self.getDistrict(i)[0][0]))
                        self.finalReSql.append(self.freezeUn2%(self.getItemStatus(i)[0][0], i, self.getDistrict(i)[0][0]))
                        self.finalReSql.append(self.freezeUn3%(i))
                elif(self.getStatus(i)[0] ==-3):
                    pass
        file = open('./freeze.sql',mode='w+')

        if(len(self.finalUpSql)):
            for final in self.finalUpSql:
                print(final)
                file.write(final+"\n")
            print("-- 回滚语句")
            file.write("-- 回滚语句\n")
            for finalRe in self.finalReSql:
                print(finalRe)
                file.write(finalRe+"\n")
            file.close()
            input("生成sql文件，请查看文件夹下的freeze.sql文件")
        else:
            input("有问题咯，队列中没有数据")


    def __del__(self):
        self.curitem.close()
        self.dbitem.close()

if __name__ == '__main__':
    a = freeze()
    a.mainFlow()