import json
import redis
import pymysql

def main():
    '''将存入redis内的数据提取出来并存入mysql数据库中'''
    rediscli = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
    mysqldb = pymysql.connect(host='localhost', user='root', password='root', database='doubandb', charset='utf8', port=3306)
    cursor = mysqldb.cursor()

    while True:
        source, data = rediscli.blpop(["douban:items"])

        item = json.loads(data)

        sql = "insert into books (`BookID`, `BookName`, `Author`, `Publisher`, `OriginName`, `Translatoer`, " \
              "`YearPublish`, `PageNumber`, `Price`, `Binding`, `Collection`, `ISBN`, `Rates`, `CommentNum`)" \
              " VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(item.get('BookID'),
               item.get('BookName'), item.get('Author'), item.get('Publisher'), item.get('OriginName'), item.get('Translatoer'), item.get('YearPublish'),
               item.get('PageNumber'), item.get('Price'),item.get('Binding'),item.get('Collection'), item.get('ISBN'),
               item.get('Rates'), item.get('CommentNum'))

        print(sql)
        cursor.execute(sql)
        mysqldb.commit()

    try:
        print
        u"Processing: %(name)s <%(link)s>" % item
    except KeyError:
        print
        u"Error procesing: %r" % item


if __name__ == '__main__':
    main()