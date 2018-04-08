import pymysql

db=pymysql.connect(host="localhost",user="root",password="root",db="mydemo",charset="utf8")

cursor=db.cursor()

#sql = "select * from stu"
#sql = "select * from stu where classid='%s'"%("python03")
data =("uu100",20,"w","python04")
sql = "insert into stu(name, age, sex, classid) values('%s','%d','%s','%s')"%(data)

try:
    cursor.execute(sql)
    print("successfully run")
    db.commit()
    '''
    while True:
        data=cursor.fetchone()
        if data == None:
            break
        print(data)
    '''
    #alist = cursor.fetchall()
    #for vo in alist:
        #print(vo)
except:
    db.rollback()
    print("sql error")

db.close()