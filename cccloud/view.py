# -*-coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import random
import json
from cccloud.alirobotapi import Send
 
def hello(request):
    return render(request,"index.html")
def alirobot(request):
    if(request.method == 'POST'):
        print("the POST method")
        concat = request.POST
        postBody = json.loads(request.body.decode())
        #print(concat)
        #print(type(postBody))
        print(postBody)
        for k,v in postBody.items():
            print(k,v)
        msg="@"+postBody["senderNick"] +"  "+ postBody["text"]["content"]
        apiurl = "https://oapi.dingtalk.com/robot/send?access_token=8f54341587be01b5e932f594b547247d307952ff866d62b870f2025044b189d0"
        Send().normal(msg, apiurl, isAtAll=False)
        return HttpResponse(str(random.randint(0,100000000)))
    else:
        return HttpResponse(str(random.randint(0,100000000)))
