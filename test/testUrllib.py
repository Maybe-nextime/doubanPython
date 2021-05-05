import urllib.request, urllib.error

# 获取一个get方式
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))  #对获取到的网页源码进行utf-8解码

# 获取一个post方式
import urllib.parse

# 变成字节文件，封装进请求
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode('utf-8'));


#超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("time out!")

#响应头问题
# response = urllib.request.urlopen("http://baidu.com", timeout=1000)
# print(response.getheaders())

# 爬虫被识破了！
# 伪装成浏览器
# url = "http://www.httpbin.org/post"
# data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
# headers={
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
#   }
# # 更多信息需要对象封装
#
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# # 请求对象构建完成，响应对象呢？
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))


url="https://www.douban.com"

headers={
     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
   }
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))