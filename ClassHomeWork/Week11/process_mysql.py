import json
import redis
import pymysql

def main():

    rediscli = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)