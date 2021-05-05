from bs4 import BeautifulSoup  # 网页解析
import re  # 正则
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite 数据库操作


def main():
    baseUrl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getData(baseUrl)
    # 2.逐一解析数据
    # 3.统一保存数据
    # savePath = r"./doubanMovieTop250.xls"
    # saveData(savePath)

    # 建议：一个功能一个函数

    # askUrl(baseUrl)


# 影片详情链接规则
findLink = re.compile(r'<a href="(.*?)">')  # 生成，创建正则表达式对象，表示规则
# 图片的链接
findImgSrc = re.compile(r'<img.*src="(.*?)"/>', re.S)  # re.S忽略换行符
# 影片的片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片的评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 找到影片的相关内容
findBd = re.compile(r'<p class="">(.*)</p>', re.S)


# 爬取网页
def getData(baseUrl):
    dataList = []
    for i in range(0, 1):
        url = baseUrl + str(i * 25)
        html = askUrl(url)  # 保存获取到的网页源码
        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")  # 形成树型结构对象
        for item in soup.find_all('div', class_="item"):
            # print(item)   #测试查看电影item
            data = []  # 保存一部电影所有信息
            item = str(item)  # 字符串化item
            print(item)
            link = re.findall(findLink, item)
            print(link)
            break

    return dataList


def saveData(savePath):
    # 3.统一保存数据
    print("..")


# 得到指定版本一个URL的网页内容
def askUrl(url):
    # 用户代理，让服务器端理解成浏览器
    head = {  # 模拟浏览器头部信息，向豆瓣发送消息
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


if __name__ == '__main__':
    main()
