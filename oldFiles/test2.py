'''
n*n/2*n/4*n/8*.....i
i不能小于10
'''
def getall(n,nall):
    nall=nall*n*n/2
    if(n/4>=10):
        if(n/8>=10):
            getall(n/4,nall)
        else:
            print(nall*n/4)
    else:
        print(nall)