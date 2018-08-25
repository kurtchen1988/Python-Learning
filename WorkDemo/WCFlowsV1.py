import pymysql
import time

class wcHuituiJiesuan:

    user = 'devread'
    passwd = 'devR3343'
    url = 'rr-9dpnbsn9mds4urq9g.mysql.rds.aliyuncs.com'


    # 需要生成的sql
    sql1 = "UPDATE db_settlement.settlement_finalstatements SET status='备案中' WHERE id in (%s);" # 结算单id
    sql2 = "UPDATE db_settlement.settlement_recordtables SET status='备案审核中' WHERE fs_id in (%s);" # 结算单id
    sql3 = "DELETE FROM db_settlement.settlement_recordtable_audits WHERE fs_id in (%s);" # 结算单id
    sql4 = "INSERT INTO db_settlement.settlement_finalstatement_logs (id ,fs_id ,org_id ,org_name, operator_id ,operator ,operation , result , create_at , update_at ) VALUES(%s,%s,null,'平台',null,'财政内网','内网备案撤销','%s', now(), now());"
    # id1, 结算单id, 理由
    idsql4 = 'select id from db_settlement.settlement_finalstatement_logs where id < 1000000000000010717 order by id desc limit 1;' # 取第一个加一id1
    sql5 = "update db_trade.zcy_orders set status=%s where id = %s;" # 订单号id
    # -5或者6分别代表取消或者开始结算
    sql6 = "INSERT INTO db_settlement.zcy_component_timeline_t (id,msg_id, biz_type, target_id, visible_label, create_at, role_category, operator, operator_id, action, detail) VALUES ('%s','%s', '10001', %s, '-1',%s, '平台', '系统', NULL, '%s', '%s');"
    # id2, msg_id(10000000加id), 订单号id，时间戳(int(time.time())), 订单取消 or 订正回退, 理由
    idsql6 = 'select id from db_settlement.zcy_component_timeline_t where id < 10000 order by id desc limit 1;' # 取第一个加一id2

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

    jiesuanID = ''
    dingdanID = []
    dingdanReason = []
    dingdanReason2 = []

    settleSql = []
    rollSql = []
    rollArray = [9]
    settlemain_id = 0
    ordermain_id = 0

    enquery1 = "select * from db_settlement.settlement_recordtables where fs_id in(结算单id);"
    enquery2 = "select * from db_settlement.purchaseplan_relation where purchaseplan_id in (采购计划id查询);" # 需要加入，在每笔结算单最后

    check0 = "SELECT distinct record_intranet_id FROM recordsync_t where record_id = (SELECT  record_no FROM db_settlement.settlement_recordtables where fs_id in(%s));" # 加入最前面，用来验证。一笔结算一个
    check1 = "select * from db_settlement.settlement_finalstatements WHERE id in(结算单id);"
    check2 = "select * from db_settlement.settlement_recordtables WHERE `fs_id` in(结算单id);" # 需要加入，在每笔结算单最后
    check3 = "select * from db_settlement.settlement_recordtable_audits WHERE `fs_id` in(结算单id);"
    check4 = "select * from db_settlement.settlement_finalstatement_logs where fs_id = 结算单id;"
    check5 = "select * from db_trade.zcy_orders where id in(订单号id);"
    check6 = "select * from db_settlement.zcy_component_timeline_t where target_id = 订单号id;"


    def __init__(self):
        self.db = pymysql.connect(host=self.url, user=self.user, password=self.passwd, port=3306, charset='utf8')
        self.cur = self.db.cursor()
        pass

    def sqlSettleData(self, settlemain_id, settlement_id, settleReason, ordermain_id, order_id,order_status, orderType, orderReason):
        self.settleSql.append(self.queryData(self.check0%settlement_id))
        self.settleSql.append(self.sql1%settlement_id)
        self.settleSql.append(self.sql2%settlement_id)
        self.settleSql.append(self.sql3%settlement_id)
        self.settleSql.append(self.sql4%(settlemain_id,settlement_id,settleReason))
        self.settleSql.append(self.sql5%(order_status, order_id))
        self.settleSql.append(self.sql6%(ordermain_id, (10000000+ordermain_id), orderType, orderReason, orderType, orderReason))

        return self.settleSql


    def rollSettleData(self, settlement_id, settle_status1,settle_status2, insertArray, settlemain_id,order_status, order_id, ordermain_id):
        self.rollSql.append(self.roll1%(settle_status1,settlement_id))
        self.rollSql.append(self.roll2%(settle_status2, settlement_id))
        self.rollSql.append(self.roll3%(insertArray[0],insertArray[1],insertArray[2],insertArray[3],insertArray[4],insertArray[0],insertArray[0],insertArray[0],insertArray[0]))
        self.rollSql.append(self.roll4%(settlemain_id))
        self.rollSql.append(self.roll5%(order_status, order_id))
        self.rollSql.append(self.roll6%(ordermain_id))

        return self.rollSql

    def rollSqlArray(self, settlement_id):
        result = self.cur.execute(self.sqlroll3%settlement_id)
        self.rollArray[0] = result[0][0]
        self.rollArray[1] = result[0][1]
        self.rollArray[2] = result[0][2]
        self.rollArray[3] = result[0][3]
        self.rollArray[4] = result[0][4]
        self.rollArray[5] = result[0][5]
        self.rollArray[6] = result[0][6]
        self.rollArray[7] = result[0][7]
        self.rollArray[8] = result[0][8]
        return self.rollArray

    def removeSettleSql(self):
        self.settleSql = []

    def removeRollSql(self):
        self.rollSql = []

    def removeRollSqlArray(self):
        self.rollArray = [9]



    def queryData(self, sql):
        result = self.cur.excute(sql)
        return result.fetchall()[0][0]
        #return 0


    def mainControl(self):

        pass

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
    a.test()
    #a.genSQL()
    #a.genRollback()
    #input("-- 按回车退出程序")