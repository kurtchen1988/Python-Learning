import pika

# 用户名与密码
user_pwd = pika.PlainCredentials('jack', '111111')

# 创建连接
connection = pika.BlockingConnection(pika.ConnectionParameters('47.96.237.51', credentials=user_pwd))

# 在连接上创建一个信道
channel = connection.channel()




# 声明交换机exchange，名字为exchange1
channel.exchange_declare(exchange='exchange1',
                         exchange_type='direct',  # 交换机类型 (默认为direct)
                         durable=True)            # 持久化

# 声明一个队列queue1，设置队列持久化，注意不要跟已存在的队列重名，否则有报错
channel.queue_declare(queue='queue1', durable=True)

# 路由的键
routing_key = 'info'

# 将交换机、队列、关键字绑定在一起，使消费者只能根据关键字从不同队列中取消息
channel.queue_bind(exchange='exchange1',
                   queue='queue1',
                   routing_key=routing_key)

# 设置消息持久化，将要发送的消息的属性标记为2，表示该消息要持久
properties = pika.BasicProperties(delivery_mode=2)

message = 'hello world'
channel.basic_publish(exchange='exchange1',     # 指明用于发布消息的交换机
                      routing_key=routing_key,  # 绑定关键字，即将message与关键字info绑定，明确将消息发送到哪个关键字的队列中
                      body=message,
                      properties=properties)
# 关闭连接
connection.close()