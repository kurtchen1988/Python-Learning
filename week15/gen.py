import random

file = open('data/x_height.txt','w+')

for i in range(18):
    file.write(str(i) + ' ' + str(random.randint(1,170))+'\n')

for i in range(18):
    file.write(str(i) + ' ' + str(random.randint(1,170))+'\n')