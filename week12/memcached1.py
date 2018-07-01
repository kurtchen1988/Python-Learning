import memcache
import pymysql


def get_data():

    # 连接Memcache
    mc = memcache.Client(['127.0.0.1'])

    cachekey = 'product_list'
    res = mc.get(cachekey)
    if res is not None:
        return res

    print('=====db=====')
    conn = pymysql.connect(host='localhost',user='root',password='root',database='test')
    cursor = conn.cursor()
    sql = 'select * from product limit 3'
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # 将数据放入memcache
    mc.set(cachekey, data,10)

    return data

print(get_data())