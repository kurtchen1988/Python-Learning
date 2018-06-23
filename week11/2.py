# 爬取指定城市天气信息
import requests
import time

url = 'https://free-api.heweather.com/s6/weather?location=北京&key=a46fd5c4f1b54fda9ee71ba6711f09cd'
res = requests.get(url)
time.sleep(2)

# 使用json格式获取数据
dlist = res.json()

# 使用换行符拆分每条城市信息
data = dlist['HeWeather6'][0]


# 输出城市信息
print('城市: ', data['basic']['location'])
print('日期: ', data['daily_forecast'][0]['date'])
print('天气: ', data['daily_forecast'][0]['cond_txt_d'], ' ~ ',data['daily_forecast'][0]['cond_txt_n'])
print(data['daily_forecast'][0]['wind_dir'], data['daily_forecast'][0]['wind_sc'], "级")