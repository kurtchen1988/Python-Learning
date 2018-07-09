import os, sys

# 检查是否root

if os.getuid() != 0:
    print('当前用户不是root，请以root身份执行脚本')
    sys.exit(1)

# 下载源码包
# http://nginx.org/download/nginx-1.14.0.tar.gz
var = input('请输入版本(默认1.13.11):')
if var == '':
    var = '1.13.11'

# 版本号的选择

# 安装目录的配置
# /usr/local/nginx

# 下载

# 解压

# 配置

# 编译