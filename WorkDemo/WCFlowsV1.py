import pymysql
import time

class wcHuituiJiesuan:

    user = 'devread'
    passwd = 'devR3343'
    url = 'rr-9dpnbsn9mds4urq9g.mysql.rds.aliyuncs.com'



    #1612230000000088852

    # 需要生成的sql
    sql1 = "UPDATE db_settlement.settlement_finalstatements SET status='备案中' WHERE id in (%s);" # 结算单id
    sql2 = "UPDATE db_settlement.settlement_recordtables SET status='备案审核中' WHERE `fs_id` in (%s);" # 结算单id
    sql3 = "DELETE FROM db_settlement.settlement_recordtable_audits WHERE `fs_id` in (%s)" # 结算单id
    sql4 = "INSERT INTO db_settlement.settlement_finalstatement_logs (`id` ,`fs_id` ,`org_id` ,`org_name` , `operator_id` ,`operator` ,`operation` , `result` , `create_at` , `update_at` ) VALUES(%s,%s,null,'平台',null,'财政内网','内网备案撤销','%s', now(), now());"
    # id1, 结算单id, 理由
    idsql4 = 'select id from db_settlement.settlement_finalstatement_logs where id < 1000000000000010717 order by id desc limit 1' # 取第一个加一id1
    sql5 = "update db_trade.zcy_orders set status=%s where id = %s;" # 订单号id
    # -5或者6分别代表取消或者开始结算
    sql6 = "INSERT INTO db_settlement.zcy_component_timeline_t (`id`,`msg_id`, `biz_type`, `target_id`, `visible_label`, `create_at`, `role_category`, `operator`, `operator_id`,`action`, `detail`) VALUES ('%s','%s', '10001', %s, '-1',%s, '平台', '系统', NULL, '%s', '%s');"
    # id2, msg_id(10000000加id), 订单号id，时间戳(int(time.time())), 订单取消 or 订正回退, 理由
    idsql6 = 'select id from db_settlement.zcy_component_timeline_t where id < 10000 order by id desc limit 1' # 取第一个加一id2

    roll1 = "UPDATE db_settlement.settlement_finalstatements SET status='%s' WHERE id in (%s);" # status1, 结算单id|这里status通过查询生成
    statusroll1 = 'select status from db_settlement.settlement_finalstatements where id in (%s);' #结算单id
    roll2 = "UPDATE db_settlement.settlement_recordtables SET status='%s' WHERE `fs_id` in (%s);" # status2, 结算单id|这里status通过查询生成
    statusroll2 = 'select status from db_settlement.settlement_recordtables where fs_id in (%s);' #结算单id
    roll3 = "INSERT INTO db_settlement.settlement_recordtable_audits (id, recordtable_id, fs_id, result, detail, start_at, end_at, create_at, update_at) VALUES (%s, %s, %s, '%s', '%s', '%s', '%s', '%s', '%s');"
    # id, recordtable_id, 结算单id, result, detail, start_at, end_at, create_at, update_at
    sqlroll3 = "select id, recordtable_id, fs_id, result, detail, start_at, end_at, create_at, update_at from db_settlement.settlement_recordtable_audits where fs_id in (%s);"     # 结算单id
    roll4 = "delete from db_settlement.settlement_finalstatement_logs where id = %s;" # id1
    roll5 = "update db_trade.zcy_orders set status= 7 where id in(%s);" # 订单号id
    roll6 = "delete from db_settlement.zcy_component_timeline_t where id = %s;" #id2
    # 需要生成的sql结束

    jiesuanID = ''
    dingdanID = []
    dingdanReason = []
    dingdanReason2 = []

    id1 = 0
    id2 = []

    enquery1 = "select * from db_settlement.settlement_recordtables where fs_id in(结算单id);"
    enquery2 = "select * from db_settlement.purchaseplan_relation where purchaseplan_id 采购计划id查询"

    check1 = "select * from db_settlement.settlement_finalstatements WHERE id in(结算单id);"
    check2 = "select * from db_settlement.settlement_recordtables WHERE `fs_id` in(结算单id);"
    check3 = "select * from db_settlement.settlement_recordtable_audits WHERE `fs_id` in(结算单id);"
    check4 = "select * from db_settlement.settlement_finalstatement_logs where fs_id = 结算单id;"
    check5 = "select * from db_trade.zcy_orders where id in(订单号id);"
    check6 = "select * from db_settlement.zcy_component_timeline_t where target_id = 订单号id;"


    def __init__(self):
        self.db = pymysql.connect(host=self.url, user=self.user, password=self.passwd, port=3306, charset='utf8')
        self.cur = self.db.cursor()
        pass

    def showData(self):

        pass



    def genSQL(self):
        try:
            self.cur.execute(self.idsql4)  # 执行拿到最后一条id的语句
            self.id1 = int(self.cur.fetchall() [0][0])+1 # 通过结果给id1赋值
            #print(self.id1)
            self.cur.execute(self.idsql6)  # 执行拿到最后一条id的语句
            tempid2 = int(self.cur.fetchall()[0][0]) + 1  # 通过结果给id2赋值
            #self.cur.close()
            #print(self.id2)
            jiesuanNum = input("请输入结算单的个数")
            for m in range(1, jiesuanNum+1):
                self.jiesuanID = int(input("请输入结算单"+str(m)+"的ID："))
                reason = input("请输入修改结算单的理由：")
                i = int(input("请输入此结算单对应的订单个数（请用数字1-9输入）："))
                for n in range(1, i+1):
                    orderID = input("请输入第"+str(n)+"个订单ID：")
                    self.dingdanID.append(orderID)
                    self.id2.append(tempid2)
                    flag = int(input("请输入您想把订单("+orderID+")修改成的状态：1.订单取消；2.订正回退 （请输入1或2）"))
                    if flag==1:
                        self.dingdanReason.append(0)
                    elif flag==2:
                        self.dingdanReason.append(1)
                    self.dingdanReason2.append(input("请输入您修改订单("+orderID+")的理由："))
                    tempid2=tempid2+1
                print("-- 开始生成"+self.jiesuanID+"的回退结算单SQL...\n\n")

                print(self.sql1%self.jiesuanID)
                print(self.sql2%self.jiesuanID)
                print(self.sql3%self.jiesuanID)
                #print(self.sql4,self.id1,self.jiesuanID, reason)
                print(self.sql4%(self.id1, self.jiesuanID, reason))
                for a in range(0, len(self.dingdanID)):
                    if(self.dingdanReason[a]==0):
                        print(self.sql5%('-5',self.dingdanID[a]))
                    elif(self.dingdanReason[a]==1):
                        print(self.sql5%('6',self.dingdanID[a]))

                for b in range(0,len(self.dingdanID)):
                    if (self.dingdanReason[b] == 0):
                        print(self.sql6 %(self.id2[b], str(int(self.id2[b])+10000000),self.dingdanID[b],str(int(time.time())),'订单取消',self.dingdanReason2[b]))
                    elif (self.dingdanReason[b] == 1):
                        print(self.sql6 % (self.id2[b], str(int(self.id2[b]) + 10000000), self.dingdanID[b], str(int(time.time())), '订正回退', self.dingdanReason2[b]))
                print("-- 回退"+self.jiesuanID+"的结算单SQL生成完毕...\n\n")
        except Exception as e:
            raise e

    '''
    def genRollback(self):

        self.cur.execute(self.statusroll1%self.jiesuanID)
        status1 = str(self.cur.fetchall()[0][0])
        # print(status1)
        self.cur.execute(self.statusroll2%self.jiesuanID)
        status2 = str(self.cur.fetchall()[0][0])
        # print(status2)
        self.cur.execute(self.sqlroll3%self.jiesuanID)
        resultall = self.cur.fetchall()
        # id, recordtable_id, fs_id, result, detail, start_at, end_at, create_at, update_at
        id = resultall[0][0]
        recordtable_id = resultall[0][1]
        fs_id = resultall[0][2]
        result = resultall[0][3]
        detail = resultall[0][4]
        start_at = resultall[0][5]
        end_at = resultall[0][6]
        create_at = resultall[0][7]
        update_at = resultall[0][8]
        #self.cur.close()
        print("-- 开始生成回滚SQL\n\n")

        print(self.roll1%(status1, self.jiesuanID))
        print(self.roll2%(status2, self.jiesuanID))
        print(self.roll3%(id, recordtable_id, fs_id, result, detail, start_at, end_at, create_at, update_at))
        print(self.roll4%self.id1)

        for a in range(0, len(self.dingdanID)):
            print(self.roll5%self.dingdanID[a])

        for b in range(0, len(self.dingdanID)):
            print(self.roll6%self.id2[b])

        print("-- 回滚SQL生成完毕")
    '''

    def mainControl(self):
        pass

    def __del__(self):
        self.cur.close()
        self.db.close()

if __name__=='__main__':
    a = wcHuituiJiesuan()
    a.genSQL()
    a.genRollback()
    input("-- 按回车退出程序")