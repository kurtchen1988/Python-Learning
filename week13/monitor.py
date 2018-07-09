import psutil

class Monitor():

    @classmethod
    def mem(cls):
        val = psutil.virtual_memory().percent
        if val > 90:
            cls.send_msg('内存使用率为{}%，超过了{}%，请关注'.format(val, max))

    @classmethod
    def cpu(cls, max):
        val = psutil.cpu_percent(1)

        if val > max:
            cls.send_msg('内存使用率为{}%，超过了{}%，请关注'.format(val, max))

    @classmethod
    def send_msg(cls, content):
        print(content)
        pass

Monitor.cpu(1)