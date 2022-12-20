import requests
import json
from lxml import etree
from selenium import webdriver
from bs4 import BeautifulSoup


query_actor = '姜文'

# 安装 chromedriver
# 确定 chrome 版本 chrome://version/
# 下载对应版本的 chromedriver.exe (http://chromedriver.storage.googleapis.com/index.html)
# 将 chromedriver.exe 放置到 chrome.exe 目录
# 将该目录路径配置到 Windows 系统环境 path 变量中
# 将 chromedriver.exe 放置到 python 根目录
#driver = webdriver.Chrome()

# 添加 User-Agent header，防止爬虫被阻止，无返回值
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}


def download(src, pid):

    data_dir = './download_data/' + str(pid) + '.jpg'

    try:
        pic = requests.get(src, timeout=10, headers=headers)

        # wb 二进制格式打开一个文件用于写入
        with open(data_dir, 'wb') as f:
            f.write(pic.content)

    except Exception:
        print('can not download file')


url_pic = 'https://www.douban.com/j/search_photo?q=' + query_actor + '&limit=20&start=0'

# selenium web
'''
driver.get(url)
full_html = driver.page_source

# 从原始 html 中提取 json 内容
soup = BeautifulSoup(full_html, 'lxml')
ss = soup.select('pre')[0]

py_resp = json.loads(ss.text)
'''

full_html = requests.get(url_pic, timeout=10, headers=headers).text
py_resp = json.loads(full_html)

for img in py_resp['images']:
    print(img['src'])
    #download(img['src'], img['id'])

#
url_book = 'https://www.douban.com/search?cat=1001&q=' + query_actor
full_html_book = requests.get(url_book, timeout=10, headers=headers).text

html_book = etree.HTML(full_html_book)

# xpath helper plug-in
title_xpath = '//*[@id="content"]/div/div[1]/div[3]/div[2]/div[@class="result"]/div[@class="content"]/div/h3/a'
titles = html_book.xpath(title_xpath)

for title in titles:
    print(title.text)




