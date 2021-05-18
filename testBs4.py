#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: zhangry
# @software: pycharm
# @file: testBs4.py
# @time: 2021/5/4 6:10 下午

# Beautiful
# -Tag,比如，就想要某个网页的一部分

from bs4 import BeautifulSoup
file = open('./baidu.html','rb')
html = file.read()
bs = BeautifulSoup(html,"html.parser")

print(bs.title) #根据标签拿到所有内容
print(bs.a)
print(bs.a.attrs)
print(bs.title.string) #没有标签，只有内容
print(bs.title.attrs)
#1.Tag 标签及其内容,但是只能拿到第一个
#2. NavigableString 标签里的内容（字符串）

#4. Comment 是一个特殊的NavigableString，输出的内容不包含注释符号
# 以上，
# --------------------------------
# 文档的遍历
print(bs.head.contents) # 返回列表，后缀获取内容，可查询BeautifulSoap官方文档
# 文档的搜索
# 1.find_all
t_list = bs.find_all("a")   #查找所有的a
import re
# 正则表达式搜索：使用search() 搜索
t_list = bs.find_all(re.compile("a"))

#方法： 传入一个函数（方法），根据函数的要求搜索
def name_is_exist(tag):
    return tag.has_attr("name")

t_list = bs.find_all(name_is_exist)

print(t_list)

# kwargs        参数
t_list = bs.find_all(id="head")
t_list = bs.find_all(class_=True)
t_list = bs.find_all(href="http://*")

#3.text参数
t_list = bs.find_all(text = "hao123")

t_list = bs.find_all(text = ["hao123","地图","贴吧"])
t_list = bs.find_all(re.compile("\d"))  #正则表达式查找包含数字的标签

#4. limit 参数
t_list = bs.find_all("a",limit = 3)

# css选择器
#返回列表
#通过标签查找
print(bs.select('title'))

#通过class查找
t_list = bs.select(".mnav")

#通过id查找
t_list = bs.select("#u1")

#通过属性查找
t_list = bs.select("a[class='bri']")

#通过子标签
t_list = bs.select("head > title")

#兄弟节点
t_list = bs.select(".mnav ~ .bri")

print(t_list[0].get_text())




