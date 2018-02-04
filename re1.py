import re1
string="taoyunjiaoyu"
#普通字符作为原子
pat="yun"
rst=re1.search(pat, string)
print(rst)
#非打印字符作为原子
#\n 换行符 \t 制表符
string='''taoyunjiaoyu
baidu
'''
pat="\n"
rst=re1.search(pat, string)
print(rst)
#通用字符作为原子
'''
\w 匹配任意一个字母数字或下划线
\W 匹配除字母，数字或下划线以外任意一个字符
\d 十进制数字
\D 除十进制数字
\s 空白字符
\S 除空白字符
'''
string="taoyunjiaoyu5465464d45yuanbidf"
pat="\s\d\d"
rst=re1.search(pat, string)
print(rst)
#原子表
string="taoyunjiaoyu5465464d45yuanbidf"
pat="tao[yun]"
pat="tao[^abs]"
rst=re1.search(pat, string)
print(rst)

#元字符
'''
.匹配除了换行符以外任意一个字符
^匹配开始位置
$匹配结束位置
*匹配0\1\多次
?匹配0\1次
+匹配1\多次
{n}匹配恰好n次
{n,}匹配至少n次
{n,m}匹配至少n次，至多m次
| 模式选择符或
()模式单元
'''
string="taoyunnnnjiaoyu5465464d45yuanbidf"
pat="bai..$"
pat="tao.*"
pat="taoyun+"
pat="yun{1,2}"
rst=re1.search(pat, string)
print(rst)
