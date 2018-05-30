import re1

#贪婪模式与懒惰模式
string="Python"
pat="p.*y"#贪婪模式
pat2="p.*?y"#懒惰模式
rst=re1.search(pat, string, re1.I)
rst2=re1.search(pat2, string, re1.I)
print(rst)
print(rst2)

#正则表达式函数
#1，match函数
string="poythonyhjskjsa"
pat="p.*?y"
rst=re1.match(pat, string, re1.I)
print(rst)
#2，search前面已经提过
#3，全局匹配函数
string="poytphonpyhjskjsa"
pat="p.*?y"
#全局匹配格式re.compile(正则表达式).findall(数据)
rst=re1.compile(pat).findall(string)
print(rst)


#实例：匹配.com和.cn网址
string="<a href='http://www.baidu.com'>百度首页</a>'"
pat="[a-zA-Z]+://[^\s]*[.com|.cn]"
rst=re1.compile(pat).findall(string)
print(rst)

#实例：匹配电话号码
string="safadsfasdf021-98762322342343sdfasdf0773-776234234asdf"
pat="\d{4}-\d{7}|\d{3}-\d{8}"
rst=re1.compile(pat).findall(string)
print(rst)
