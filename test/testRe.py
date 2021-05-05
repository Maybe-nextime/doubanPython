#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: zhangry
# @software: pycharm
# @file: testRe.py
# @time: 2021/5/5 11:03 下午

#正则表达式：字符串模式（判断字符串符合一定的标准）
import re
# 创建模式对象
pat = re.compile("AA") # 此处的AA是字符表达式，验证其他的字符串
# m = pat.search("CBA") # search字符串被校验的内容
# m = pat.search("ABCAA") # search字符串被校验的内容
# m = pat.search("ABCAADDCCAA") # search字符串被校验的内容

#没有模式对象
# m = re.search("asd","Aasd") # 前面的字符串是规则，后面的是被校验的对象

# findall
# m = re.findall("a","ASDASDFasd") # 返回列表

m = re.findall("[A-Z]","ASDweDSD")
# m = re.findall("[A-Z]+","ASDweDSD")

#sub 替换
# m = re.sub("a","A",r"asdadada") #被替换的字符，替换的字符，被校验的字符串

# 建议在正则表达式中，被比较的字符串中加r，不用担心转义字符问题
print(m)

