import requests
import re

url = "http://www.jingcaiyuedu.com/novel/GLSmM4.html"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0", }
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

html = response.text
title = re.findall(r'<meta property="og:title" content="(.*?)"/>', html)[0]
dl = re.findall(r'<dl class="panel-body panel-chapterlist">.*?</dl>', html, re.S)[1]
chapter_list = re.findall(r'href="(.*?)">(.*?)<', dl)

f = open(f"{title}.txt", 'w', encoding="utf-8")

for i in chapter_list:
    book_url, book_name = i
    book_url = f"http://www.jingcaiyuedu.com{book_url}"

    book_response = requests.get(book_url, headers=headers)
    book_response.encoding = 'utf-8'
    book_html = book_response.text
    book_content = re.findall(r'<div class="panel-body" id="htmlContent">(.*?)</div>', book_html, re.S)[0]

    # 数据清洗
    book_content = book_content.replace(' ', '')
    book_content = book_content.replace('&nbsp;', '')
    book_content = book_content.replace('<br />', '')
    book_content = book_content.replace('<br/>', '')
    book_content = book_content.replace('<p>', '')
    book_content = book_content.replace('</p>', '\n')

    # 写入txt文件
    f.write(f"{book_name}\n")
    f.write(f"{book_content}\n")
    f.write("\n")

    print(book_url)
    print(i[1])

    # 调试用
    # print(book_content)
    # exit()
