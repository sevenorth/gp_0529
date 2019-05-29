# -*- coding:utf8 -*-
import urllib.request
import urllib.parse

url = "https://baidu.com"
headers = {}
headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding":"utf-8",
    "Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
    "Connection":"keep-alive",
    "Host":"c.highpin.cn",
    "Referer":"http://c.highpin.cn/",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
}
data = {}
data['appchg'] = 'AppStore'
data['apptype'] = '21'
#数据编码
data = urllib.parse.urlencode(data)
req = urllib.request.Request(url, data)
#打开地址并且赋值给变量
ResponseStr = urllib.request.urlopen(req)
ResponseStr = ResponseStr.read()

ResponseStr = ResponseStr.decode('unicode_escape')
print(ResponseStr)