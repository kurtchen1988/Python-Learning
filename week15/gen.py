import random

cities = ['杭州市',
'宁波市',
'绍兴市',
'温州市',
'台州市',
'湖州市',
'嘉兴市',
'金华市',
'舟山市',
'衢州市',
'丽水市',
'余姚市',
'乐清市',
'临海市',
'温岭市',
'永康市',
'瑞安市',
'慈溪市',
'义乌市',
'上虞市',
'诸暨市',
'海宁市',
'桐乡市',
'兰溪市',
'龙泉市',
'建德市',
'富德市',
'富阳市',
'平湖市',
'东阳市',
'嵊州市',
'奉化市',
'临安市',
'江山市']
file = open('data/cities.txt','w+', encoding='utf-8')
file.write('排名 城市 平均工资'+'\n')

for i in range(len(cities)):
    file.write(str(i) + ' '+random.choice(cities)+' '+ str(random.randint(1,10000))+'\n')
