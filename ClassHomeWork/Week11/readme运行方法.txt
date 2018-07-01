1.在mysql中创建一个编码为UTF8的数据库doubandb

2.用database.sql导入数据表

3.确保redis和mysql在开启状态

4.将process_mysql.py跑起来，接着用两个进程同时跑doubanspider.py和doubanspidermaster.py

