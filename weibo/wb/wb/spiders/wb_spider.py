# encoding = "utf-8"
import scrapy
from bs4 import BeautifulSoup


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
            keyword = t.find("td", class_="td-02").a.string
            value = t.find("td", class_="td-02").span
            value = str(value).replace("<span>","").replace("</span>","")
            # print(str(value).replace("<span>","").replace("</span>",""))
            print(index, keyword,value)
            print("-"*80)
