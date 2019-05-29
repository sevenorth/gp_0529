# _*_ coding:utf8
import urllib.request
import urllib.parse

url = "https://baidu.com"
data = {}
data['loginname'] = 'student08@qq.com'
data['password'] = '11111'
#对请求数据进行编码
data = urllib.parse.urlencode(data)
#将数据和url进行链接
request = url+'?'+data
requestResponse = urllib.request.urlopen(request)
RequsetStr = requestResponse.read()
#打印数据
RequsetStr = RequsetStr.decode('unicode_escape')
print(RequsetStr)