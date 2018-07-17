import re
'''
data = '10.26'
a = []
b = []
c = []


if re.match('\d{4,}\w*', data):
    first = re.findall('(\d{4,})\w*', data)
    first = first[0]
    first = float(first)
    first = round(first/1000,1)
    print(first)

elif re.match('\d{1,2}\.\d*T', data):
    second = re.findall('(\d{1,2}\.\d*)T', data)
    second = second[0]
    second = float(second)
    second = round(second, 1)
    print(second)

elif re.match('\d{1,2}\.\d{2,}',data):
    third = re.findall('\d{1,2}\.\d{2,}', data)
    third = third[0]
    third = float(third)
    third = round(third, 1)
    validate = [None] * 6
    print(validate)

    print(third)
'''
'''
data = '07'

print(data)

data = int(data)

print(data)

data = str(data)

print(data)
'''

import sys
from time import sleep


def viewBar(i):
    """
    进度条效果
    :param i:
    :return:
    """
    output = sys.stdout
    for count in range(0, i + 1):
        second = 0.1
        sleep(second)
        output.write('\rcomplete percent ----->:%.0f%%' % count)
    output.flush()


viewBar(100)