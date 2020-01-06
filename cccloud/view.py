# -*-coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import random
import json
from cccloud.alirobotapi import Send
from tools.usegit import GitRepository
 
def hello(request):
    return render(request,"index.html")
def gitpull(request):
    try:
        if request.method == 'GET':
            name = request.GET.get('name', default='cccode')
            localpath = ""
            repo_url = ""
            if name == "cccode":
                localpath = r"C:\cccode\cccode"
                repo_url = r"https://github.com/husky8/cccode.git"
            if name == "cccloud":
                localpath = r"C:\Users\Administrator\cccloud"
                repo_url = r"https://github.com/husky8/cccloud.git"
            if localpath != "":
                GitRepository(localpath,repo_url).pull()
                return HttpResponse("mabey ok")
    except:
        return HttpResponse("mabey not ok")
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
