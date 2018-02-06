import re
import urllib.request

class getCSDNContent():

url="http://blog.csdn.net/"

    def getContent(self):
        data=urllib.request.urlopen(url).read().decode("utf-8")

    def filterContent(self):
        pass


    def saveContent(self):
        pass