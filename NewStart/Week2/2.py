'''
class File:

    def __init__(self, name):
        self.name=name
        print("open file", self.name)


    def __del__(self):
        print("close file", self.name)
'''
'''
class Stu:
    name="zhangsan"
    age=20

    def __str__(self):
        return "name:%s;age:%d"%(self.name,self.age)

s = Stu()
print(s)
'''
class Demo:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return "Demo(%d,%d)"%(self.x,self.y)

    def __add__(self, other):
        return Demo(self.x+other.x, self.y+other.y)