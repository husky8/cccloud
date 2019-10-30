# -*-coding:utf-8 -*-
import requests
import json


class Send():
    """官方文档 https://open-doc.dingtalk.com/docs/doc.htm?spm=a219a.7629140.0.0.karFPe&treeId=257&articleId=105735&docType=1 """

    def normal(self, msg, apiurl,  atList=[], isAtAll=False):
        if type(atList) != type([1, 2, 3]):
            return "atList应为列表"
        HEADERS = {
            "Content-Type": "application/json ;charset=utf-8 "
        }
        str_data = {
            "msgtype": "text",
            "text": {"content": msg+"."},
            "at": {
                "atMobiles": atList,
                "isAtAll": isAtAll
            }
        }
        json_data = json.dumps(str_data)
        res = requests.post(apiurl, data=json_data, headers=HEADERS)
        return res.text

    def link(self, apiurl, title, text="", picUrl="", messageUrl="http://www.baidu.com"):
        HEADERS = {
            "Content-Type": "application/json ;charset=utf-8 "
        }
        str_data = {
            "msgtype": "link",
            "link": {
                "title": title,
                "text": text,
                "picUrl": picUrl,
                "messageUrl": messageUrl
            }
        }
        json_data = json.dumps(str_data)
        res = requests.post(apiurl, data=json_data, headers=HEADERS)
        return res.text

    def MarkDown(self, apiurl, title, text, atList=[],isAtAll=False):
        # "text": "#### 杭州天气  \n > 9度， 西北风1级，空气良89，相对温度73%\n\n > ![screenshot](http://i01.lw.aliimg.com/media/lALPBbCc1ZhJGIvNAkzNBLA_1200_588.png)\n  > ###### 10点20分发布 [天气](http://www.thinkpage.cn/) "
        if type(atList) != type([1, 2, 3]):
            return "atList应为列表"
        HEADERS = {
            "Content-Type": "application/json ;charset=utf-8 "
        }
        str_data = {
            "msgtype": "markdown",
            "markdown": {"title": title,
                         "text":text,
                         },
            "at": {
                "atMobiles": atList,
                "isAtAll": isAtAll
            }
        }
        json_data = json.dumps(str_data)
        res = requests.post(apiurl, data=json_data, headers=HEADERS)
        return res.text


if __name__ == '__main__':
    # url = 'https://oapi.dingtalk.com/robot/send?access_token=0c57dacf315f6b76a7fa869819820fa108b9eb4111920fb353b2dd22d2d6efd4'
    url="https://oapi.dingtalk.com/robot/send?access_token=8f54341587be01b5e932f594b547247d307952ff866d62b870f2025044b189d0"
    

