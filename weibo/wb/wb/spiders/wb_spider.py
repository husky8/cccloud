# encoding = "utf-8"
import os
import sys
os.chdir(os.path.dirname(sys.argv[0]))
project_dir = os.path.split(os.getcwd())
project_dir = os.path.split(project_dir[0])
sys.path.append(project_dir[0])
os.path.abspath("C:\Users\Administrator\cccloud")
os.chdir(project_dir[0])
import time
import scrapy
from bs4 import BeautifulSoup
from tools.usemysql import executesql


class WbSpider(scrapy.spiders.Spider):
    name = "weibo"
    allowed_domains = ["s.weibo.com","captcha.weibo.com"]
    start_urls = [
        "https://s.weibo.com/top/summary?cate=realtimehot".replace(" ","")
    ]

    def parse(self, response):
        rhtmls = response.xpath("//tbody/tr").extract()
        self.getData(rhtmls)

    def getData(self, rhtmls):
        for rhtml in rhtmls:
            # print("-*100")
            # print(rhtml)
            # print("-*100")
            t = BeautifulSoup(rhtml, 'lxml')

            index = t.find("td", class_="td-01").string
            title = t.find("td", class_="td-02").a.string
            value = t.find("td", class_="td-02").span
            value = str(value).replace("<span>","").replace("</span>","")
            # print(str(value).replace("<span>","").replace("</span>",""))
            executesql("""INSERT INTO weibohothistory VALUES({id},{title},{index} ,{value} now() );""".format(
                id = hash(time.time()),title=title,index=index,value=value
            ))
