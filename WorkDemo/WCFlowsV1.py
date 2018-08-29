import pymysql
import time
import json

class wcHuituiJiesuan:

    user = 'devread'
    passwd = 'devR3343'
    url = 'rr-9dpnbsn9mds4urq9g.mysql.rds.aliyuncs.com'


    # 需要生成的sql
    check0 = "SELECT distinct record_intranet_id FROM db_settlement.recordsync_t where record_id = (SELECT  record_no FROM db_settlement.settlement_recordtables where fs_id in(%s));" # 查询内网是否结算成功
    sql1 = "UPDATE db_settlement.settlement_finalstatements SET status='备案中' WHERE id in (%s);" # 结算单id
    sql2 = "UPDATE db_settlement.settlement_recordtables SET status='备案审核中' WHERE fs_id in (%s);" # 结算单id
    sql3 = "DELETE FROM db_settlement.settlement_recordtable_audits WHERE fs_id in (%s);" # 结算单id
    sql4 = "INSERT INTO db_settlement.settlement_finalstatement_logs (id ,fs_id ,org_id ,org_name, operator_id ,operator ,operation , result , create_at , update_at ) VALUES(%s,%s,null,'平台',null,'财政内网','内网备案撤销','%s', now(), now());"
    # id1, 结算单id, 理由
    idsql4 = 'select id from db_settlement.settlement_finalstatement_logs where id < 1000000000000010717 order by id desc limit 1;' # 取第一个加一id1
    sql5 = "update db_trade.zcy_orders set status=%s where id = %s;" # 订单号id
    # -5或者6分别代表取消或者开始结算
    sql6 = "INSERT INTO db_settlement.zcy_component_timeline_t (id,msg_id, biz_type, target_id, visible_label, create_at, role_category, operator, operator_id, action, detail) VALUES ('%s','%s', '10001', '%s', '-1','%s', '平台', '系统', NULL, '%s', '%s');"
    # id2, msg_id(10000000加id), 订单号id，时间戳(int(time.time())), 订单取消 or 订正回退, 理由
    idsql6 = 'select id from db_settlement.zcy_component_timeline_t where id < 10000 order by id desc limit 1;' # 取第一个加一id2
    issql7 = "SELECT payment_snapshot FROM db_settlement.settlement_finalstatement_business where fs_id = %s" # 查询
    sql7 = "select * from db_settlement.purchaseplan_relation where purchaseplan_id in (%s);"  # 需要加入，在每笔结算单最后，需要查询采购计划id
    sql8 = "select record_sync_id from db_settlement.settlement_recordtables WHERE `fs_id` in(%s);"  # 需要加入，在每笔结算单最后，结算单id

    roll1 = "UPDATE db_settlement.settlement_finalstatements SET status='%s' WHERE id in (%s);" # status1, 结算单id|这里status通过查询生成
    statusroll1 = 'select status from db_settlement.settlement_finalstatements where id in (%s);' #结算单id
    roll2 = "UPDATE db_settlement.settlement_recordtables SET status='%s' WHERE `fs_id` in (%s);" # status2, 结算单id|这里status通过查询生成
    statusroll2 = 'select status from db_settlement.settlement_recordtables where fs_id in (%s);' #结算单id
    roll3 = "INSERT INTO db_settlement.settlement_recordtable_audits (id, recordtable_id, fs_id, result, detail, start_at, end_at, create_at, update_at) VALUES (%s, %s, %s, '%s', '%s', '%s', '%s', '%s', '%s');"
    # id, recordtable_id, 结算单id, result, detail, start_at, end_at, create_at, update_at
    sqlroll3 = "select id, recordtable_id, fs_id, result, detail, start_at, end_at, create_at, update_at from db_settlement.settlement_recordtable_audits where fs_id in (%s);"     # 结算单id
    roll4 = "delete from db_settlement.settlement_finalstatement_logs where id = %s;" # id1
    roll5 = "update db_trade.zcy_orders set status= %s where id in(%s);" # 订单号id
    roll6 = "delete from db_settlement.zcy_component_timeline_t where id = %s;" #id2
    # 需要生成的sql结束


    file = None
    settleSql = []
    rollSql = []
    rollArray = []
    purchase = {}
    purchase_idArray = []
    purchase_id = None
    settlemain_id = 0
    ordermain_id = 0



    def __init__(self):
        self.db = pymysql.connect(host=self.url, user=self.user, password=self.passwd, port=3306, charset='utf8')
        self.cur = self.db.cursor()
        pass

    def sqlSettleData(self, settlemain_id, settlement_id, settleReason):
        self.settleSql.append(self.queryData(self.check0%settlement_id))
        self.settleSql.append(self.sql1%settlement_id)
        self.settleSql.append(self.sql2%settlement_id)
        self.settleSql.append(self.sql3%settlement_id)
        self.settleSql.append(self.sql4%(settlemain_id,settlement_id,settleReason))


        return self.settleSql

    def sqlOrderData(self, ordermain_id, order_id,order_status, orderType, orderReason):
        self.settleSql.append(self.sql5 % (order_status, order_id))
        self.settleSql.append(
        self.sql6 % (ordermain_id, (10000000 + ordermain_id), order_id, str(int(time.time()))+'000', orderType, orderReason))
        #self.settleSql.append(self.sql7)

        return self.settleSql

    def sqlQueryData(self, settlement_id):
        self.settleSql.append(self.sql8 % settlement_id)

        return self.settleSql

    def sqlPurchase(self, purchaseId):
        self.settleSql.append(self.sql7%purchaseId)

        return self.settleSql

    def rollSettleData(self, settlement_id, settle_status1,settle_status2, insertArray, settlemain_id):
        self.rollSql.append(self.roll1%(settle_status1, settlement_id))
        self.rollSql.append(self.roll2%(settle_status2, settlement_id))
        self.rollSql.append(self.roll3%(insertArray[0],insertArray[1],insertArray[2],insertArray[3],insertArray[4],insertArray[5],insertArray[6],insertArray[7],insertArray[8]))
        self.rollSql.append(self.roll4%(settlemain_id))

        return self.rollSql

    def rollOrderData(self, order_status, order_id, ordermain_id):
        self.rollSql.append(self.roll5 % (order_status, order_id))
        self.rollSql.append(self.roll6 % (ordermain_id))

        return self.rollSql

    def rollSqlArray(self, settlement_id):
        self.cur.execute(self.sqlroll3%settlement_id)
        roll = self.cur.fetchall()
        self.rollArray.append(roll[0][0])
        self.rollArray.append(roll[0][1])
        self.rollArray.append(roll[0][2])
        self.rollArray.append(roll[0][3])
        self.rollArray.append(roll[0][4])
        self.rollArray.append(roll[0][5])
        self.rollArray.append(roll[0][6])
        self.rollArray.append(roll[0][7])
        self.rollArray.append(roll[0][8])
        return self.rollArray

    def purchaseQuery(self, settlement_id):
        self.purchase = self.queryData(self.issql7%settlement_id)
        self.purchase = json.loads(self.purchase)
        self.purchase = self.purchase["pplans"]
        for id in self.purchase:
            self.purchase_idArray.append(str(id["pplanId"]))
        self.purchase_id = ','.join(self.purchase_idArray)
        return self.purchase_id

    def removeSettleSql(self):
        self.settleSql = []

    def removeRollSql(self):
        self.rollSql = []

    def removeRollSqlArray(self):
        self.rollArray = []

    def removePurchaseId(self):
        self.purchase_id = None


    def queryData(self, sql):
        self.cur.execute(sql)
        a = self.cur.fetchall()
        #print(a)
        return a[0][0]

    def openFile(self):
        self.file = open("./settlement" + time.strftime('%d%H%M%S') + ".log", "w+")

    def writeToFile(self):

        if len(self.settleSql) != 0:
            self.file.write("-- 开始生成结算单回退SQL\n\n")
            for sql in self.settleSql:
                self.file.write(str(sql)+"\n")
            self.file.write("-- 回退SQL生成完毕\n\n")
        else:
            print("SQL生成数组长度为0，有问题！")

        if len(self.rollSql) != 0:
            self.file.write("-- 开始生成回滚语句\n\n")
            for rollsql in self.rollSql:
                self.file.write(str(rollsql)+"\n")
            self.file.write("-- 回滚SQL生成完毕\n\n")
        else:
            print("SQL回滚数组长度为0，有问题！")

    def saveFile(self):
        self.file.close()


    def mainControl(self):
        self.openFile()
        settleNum = input("请输入回退结算单的个数：")
        settlemain = self.queryData(self.idsql4)
        ordermain = self.queryData(self.idsql6)

        for num in range(1,int(settleNum)+1):

            settlementID = input("请输入第"+str(num)+"个结算单号码：")
            setReason = input("请输入回退结算单的原因：")
            settlemain=settlemain+1
            self.sqlSettleData(settlement_id=settlementID,settlemain_id=settlemain, settleReason=setReason)
            #self.sqlQueryData(settlementID)

            self.rollSettleData(settlement_id=settlementID,settle_status1=self.queryData(self.statusroll1%settlementID),settle_status2=self.queryData(self.statusroll2%settlementID),insertArray=self.rollSqlArray(settlementID), settlemain_id=settlemain)
            numOrder = input("请输入订单的个数：")
            for orders in range(1, int(numOrder)+1):
                ordermain = ordermain+1
                orderID = input("请输入"+settlementID+"的第"+str(orders)+"个订单号码：")
                orderFlag = int(input("请输入您想把订单(" + orderID + ")修改成的状态：1.订单取消；2.订正回退 （请输入1或2）"))
                ordReason = input("请输入您修改订单("+ orderID +")的理由：")
                self.rollOrderData(order_status=0, order_id=orderID,ordermain_id=ordermain)
                if orderFlag == 1:
                    orderType = '订单取消'
                    self.sqlOrderData(ordermain_id=ordermain, order_id=orderID, order_status=-5, orderType=orderType, orderReason=ordReason)

                elif orderFlag == 2:
                    orderType = '订正回退'
                    self.sqlOrderData(ordermain_id=ordermain, order_id=orderID, order_status=6, orderType=orderType, orderReason=ordReason)

            self.sqlPurchase(self.purchaseQuery(settlementID))

            self.settleSql.append(self.queryData(self.sql8%settlementID)) # 把查询的sync_id写入数组

            self.writeToFile()
            self.removeSettleSql()
            self.removeRollSql()
            self.removeRollSqlArray()
        self.saveFile()
        input("生成SQL完毕，请查看生成的sql文件")



    def __del__(self):

        self.cur.close()
        self.db.close()
        pass

    def test(self):
        self.sqlSettleData(settlemain_id=23,settlement_id=45,settleReason="this is test", ordermain_id=50, order_id=60, order_status="test",orderType="back", orderReason="okok")
        self.rollSettleData(settlement_id=23, settle_status1="test", settle_status2="test", insertArray=['test','test','test','test','test','test','test','test','test'],
                            settlemain_id=20, order_status="test", order_id=30, ordermain_id=40)
        self.removeSettleSql()
        self.removeRollSql()
        print(self.settleSql)
        print(self.rollSql)

if __name__=='__main__':
    a = wcHuituiJiesuan()
    a.mainControl()
    #a.genSQL()
    #a.genRollback()
    #input("-- 按回车退出程序")