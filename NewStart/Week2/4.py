'''
a=[10,20,30]
y = iter(a)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
'''

class A:
    def __init__(self):
        self.x=0

    def __next__(self):
        self.x +=1
        if self.x>10:
            raise StopIteration
        return self.x

    def __iter__(self):
        return self

a=A()

for i in a:
    print(i)