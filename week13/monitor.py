import psutil, time

class Monitor():

# pscp.exe monitor.py root@47.96.237.51:/root

    cpu_data = []

    @classmethod
    def mem(cls, max=90):
        val = psutil.virtual_memory().percent
        if val > max:
            cls.send_msg('内存使用率为{:1f}%，超过了{}%，请关注'.format(val, max))

    @classmethod
    def cpu(cls, max):
        val = psutil.cpu_percent(1)

        cls.cpu_data.append(val)

        print(cls.cpu_data)

        if len(cls.cpu_data) >= 3:

            avg = sum(cls.cpu_data) / len(cls.cpu_data)

            cls.cpu_data.pop(0)

            if avg > max:
                cls.send_msg('内存使用率为{:1f}%，超过了{}%，请关注'.format(avg, max))

    @classmethod
    def send_msg(cls, content):
        print(content)
        cls.mail(content)
        cls.wechat(content)
        pass

    @classmethod
    def mail(cls, content):
        import smtplib
        from email.mime.text import MIMEText
        from email.utils import formataddr

        nickname='监控程序'
        sender = '76251098@qq.com'
        password = 'usdpmgphuhyvbhjd'
        receiver = 'kurtcobain1988824@hotmail.com'

        msg = MIMEText(content,'html','utf-8')
        msg['From'] = formataddr([nickname, sender])
        msg['Subject'] = '自动报警'

        server = smtplib.SMTP_SSL('smtp.qq.com',465)

        try:
            server.login(sender, password)
            server.sendmail(sender,[receiver],msg.as_string())
        except Exception as ex:
            print(ex)
        finally:
            server.quit()

        pass

    @classmethod
    def wechat(cls, content):

        from wechatpy import WeChatClient
        import datetime

        client = WeChatClient('wx5e3d9173a2186c46','f99a608cf4e5355fdd0c08daefd25572')
        template_id = 'O39JTNpcG1mzchii5UdlZZ3GHIuGTuNwzzpJtSkiySY'
        openid = 'oUfpW0vfMT0ptnhvx1yecCnh70_M'

        data = {
            'msg':{"value":content, "color":"#173177"},
            'time':{"value":datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "color":"#173177"},
        }

        client.message.send_template(openid,template_id, data)
        pass

#Monitor.wechat('CPU超过90%')


while True:

    Monitor.mem(5)
    Monitor.cpu(5)
    time.sleep(3)
