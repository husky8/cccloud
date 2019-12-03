#encoding = "utf-8"
import scrapy
import json
from bs4 import BeautifulSoup
from scrapy.selector import  Selector
class WbSpider(scrapy.spiders.Spider):

    name = "weibo"
    allowed_domains = ["s.weibo.com/"]
    start_urls = [
        "https://s.weibo.com/top/summary?cate=realtimehot"
    ]

    # def start_requests(self):
    #     return [scrapy.FormRequest("http://www.example.com/login",
    #                                # formdata={'user': 'john', 'pass': 'secret'},
    #                                callback=self.parse())]

    def parse(self,response):
        rhtmls = response.xpath("//tbody/tr").extract()
        self.getData(rhtmls)

    def getData(self,rhtmls):
        for rhtml in rhtmls:
            t = BeautifulSoup(rhtml,'lxml')

            index = t.find("td",class_ = "td-01").string
            keyword = t.find("td",class_="td-02").a.string
            # href = t.find("p",class_="star_name").a.get("herf")
            # isnew = t.find("p",class_="star_name").i
            # if isnew != None:
            #     isnew_str = isnew.string
            # else:
            #     isnew_str = ""
            # searchs = t.find("p",class_="star_name").span.string
            print(index,keyword
                  # keyword,href,isnew_str,searchs
                  )
            print("-*100")
if __name__ == '__main__':
    WbSpider().start_requests()