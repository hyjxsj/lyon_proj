#-*- coding:utf-8 -*-
__author = "huia"

import requests
from requests.exceptions import RequestException
import random
import re
from bs4 import BeautifulSoup

def get_one_page(url):
    my_headers = [
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
        'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
    ]
    headers = {'user-Agent': random.choice(my_headers)}
    try:
        response = requests.get(url,headers=headers)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response
        return None
    except RequestException:
        return None
def parse_one_page(text):
    pattern = re.compile('<a.*?title="(.*?)">.*?</a>',re.S)
    soup = BeautifulSoup(text,'lxml')
    results = soup.find_all('a')
    print(type(results))
    res = re.findall(pattern,str(results))
    print(res)
    for index,rr in enumerate(res):
        print(index,rr)
def parse_one_page2(text):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                          +'.*?integer">(.*?)</i.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,text)
    print(items)
    print('格式化后如下'.center(50,'-'))
    for item in items:
        yield {
            'index':items[0],
            'index':,
            'index':,
            'index':,
            'index':,
            'index':
        }

def main():
    url = "http://maoyan.com/board/4?"
    html = get_one_page(url)
    print(html.status_code)
    print(html.text)
    parse_one_page2(html.text)


if __name__ == '__main__':
    main()

