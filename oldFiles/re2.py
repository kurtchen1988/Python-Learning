import re1

string="taoyunnnnjiaoyu5465464d45yuanbidf"
pat="bai..$"
pat="tao.*"
pat="taoyun+"
pat="yun{1,2}"
rst=re1.search(pat, string)
print(rst)

#模式修正符
'''
I 匹配时忽略大小写*
M 多行匹配*
L 本地化识别匹配
U Unicode
S 让.匹配包括换行符*
'''
string="Python"
pat="pyt"
rst=re1.search(pat, string, re1.I)
print(rst)
