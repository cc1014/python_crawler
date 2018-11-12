#!/usr/bin/env python
# coding: utf-8

# In[85]:


import urllib.request as request
import json
import xlwt
url_number={57516,57348,57522,57536,57518,57511,57520,57333,57502,57425,57523,57512,57517,57338,57426,57519,57537,57505,57438,57510,57509,57432,57349,57345,57525,57635,57506,57633,57513,57339,57437,57409,57514,57612}
   
try:
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('rainfall')
        
    head = ['日期', '时间', '省份', '城市', '降雨量(单位mm)'] 
    for h in range(len(head)):
        sheet.write(0, h, head[h])
    
    row = 1 
    for i in url_number:
        url = "%s%s"%("http://www.nmc.cn/f/rest/real/",i)
        print(url)
        weather_content = request.urlopen(url).read()
        date = json.loads(weather_content.decode('utf8'))['publish_time'].split()[0]
        time = json.loads(weather_content.decode('utf8'))['publish_time'].split()[1]
        province = json.loads(weather_content.decode('utf8'))['station']['province']
        city = json.loads(weather_content.decode('utf8'))['station']['city']
        rain = json.loads(weather_content.decode('utf8'))['weather']['rain']
        print(date)
        print(time)
        print(province)
        print(city)
        print(rain)
        
        sheet.write(row, 0, date)
        sheet.write(row, 1, time)
        sheet.write(row, 2, province)
        sheet.write(row, 3, city)
        sheet.write(row, 4, rain)
        row = row + 1
    
    workbook.save('weather_table.xlsx')
    print('写入excel成功')
except Exception:
    print('写入excel失败')


# In[ ]:




