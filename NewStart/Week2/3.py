'''
class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0

    def setSize(self,size):
        self.width,self.height = size

    def getSize(self):
        return self.width, self.height

    size = property(getSize, setSize)

r=Rectangle()
r.width=100
r.height=50
print(r.width,r.height)

r.size =100, 500
print(r.size)
'''
'''
class A:
    @staticmethod
    def fun():
        print("aaaaaaaaaaaaaaaa")
    fun = staticmethod(fun)

    @classmethod
    def demo(self):
        print("bbbbbbbbbbbbbbbb")
    demo=classmethod(demo)

A.fun()
A.demo()
'''
class B:
    name="zhangsan"
    __age=20

    def fun1(self):
        print("aaaa")

    def __dd(self):
        print("ccc")

b = B()
print(hasattr(b,"name"))
print(hasattr(b,"__age"))
print(hasattr(b,"fun1"))
print(hasattr(b,"__dd"))