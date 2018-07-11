import re

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