import json
import redis
import pymysql

def main():

    rediscli = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
    mysqldb = pymysql.connect(host='localhost', user='root', password='root', database='doubandb', charset='utf8', port=3306)
    cursor = mysqldb.cursor()

    while True:
        source, data = rediscli.blpop(["demo:items"])

        item = json.loads(data)

        sql = "insert into doubandb VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"%(item.get('BookID'),
               item.get('BookName'), item.get('Author'), item.get('OriginName'), item.get('Translatoer'), item.get('YearPublish'),
               item.get('PageNumber'), item.get('Price'),item.get('Binding'),item.get('Collection'), item.get('ISBN'),
               item.get('Rates'), item.get('CommentNum'))

        cursor.execute(sql)
        mysqldb.commit()