# 引入库
import time
import requests
# 正则表达式
import re
# 应对动态延迟
from selenium import webdriver
# 写网站站点
url = "https://doupocangqiong1.com/1/"
# 写入headers模拟浏览器上网,避免出现个别网站拒绝访问的情况
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0", }
# get发送请求
response = requests.get(url, headers=headers)
# 将网页编码方式转换为utf-8
response.encoding = 'utf-8'
# 网站源码
html = response.text
# re.findall获取小说的名字
title = re.findall(r'<meta property="og:title" content="(.*?)"/>', html)[0]
# 获取每一章的信息(章节的url)
dl = re.findall(r'<ul class="dirlist three clearfix">.*?</ul>', html, re.S)[0]
chapter_list = re.findall(r'href="(.*?)" title="(.*?)" target="_blank">(.*?)<', dl)

# 新建文件保存小说内容
f = open(f"{title}.txt", 'w', encoding="utf-8")

# 循环每一个章节,分别去下载
for i in chapter_list:
    # 章节地址和名
    book_url = i[0]
    book_name = i[2]

    # 拼接正确章节地址
    book_url = f"https://doupocangqiong1.com{book_url}"

    # 等待文章内容加载
    driver = webdriver.PhantomJS()
    driver.get(book_url)
    book_html = driver.execute_script('return document.documentElement.outerHTML')

    # 获取章节
    # book_response = requests.get(book_url, headers=headers)
    # book_response.encoding = 'utf-8'
    # book_html = book_response.txt

    # 提取章节内容
    book_content = re.findall(r'<div class="content" id="chaptercontent">(.*?)</div>', book_html, re.S)[0]

    # 清洗提取的数据
    # 将其中内容的空格部分替换成空
    book_content = book_content.replace(' ', '')
    # 将其中内容的&nbsp;部分替换成空
    book_content = book_content.replace('&nbsp;', '')
    # 将其中内容的<br />部分替换成空
    book_content = book_content.replace('<br />', '')
    # 将其中内容的<br/>部分替换成空
    book_content = book_content.replace('<br/>', '')
    # 将其中内容的<p>部分替换成空
    book_content = book_content.replace('<p>', '')
    # 将其中内容的</p>部分替换成换行符
    book_content = book_content.replace('</p>', '\n')

    # 写入
    f.write(f"{book_name}\n")
    f.write(f"{book_content}\n")
    f.write("\n")
    print(book_url)
    driver.quit()
    # 调试用
    # print(book_content)
    # exit()
