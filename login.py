import httpx
import re
from win10toast import ToastNotifier
import sys
import time
servicelList:list=["学校互联网服务","联通互联网服务","移动互联网服务","电信互联网服务","校内免费服务"]
queryString:str=""
operatorPwd:str=""
operatorUserId:str=""
validcode:str=""
passwordEncrypt:str=""
oldUrl:str="http://123.123.123.123/?mode=history"
toast = ToastNotifier()

def main(userId:int, password:str,serviceIndex:int=5):
    if serviceIndex<1 or serviceIndex>5:
        showMsg("我不是告诉你在1-5以内吗")
        quit()
    serviceIndex-=1
    userId
    password
    service=servicelList[serviceIndex]
    try:
        newUrl=setNewUrl()
        showMsg("连接中...",2)
        headers=setHeaders(newUrl)
        queryString=setQueryString(newUrl)
        Ip=setIp(newUrl)
        loginUrl=setLoginUrl("http://{}/eportal/InterFace.do?method=login",Ip)
        login(
            userId,
            password,
            service,
            queryString,
            operatorPwd,
            operatorUserId,
            validcode,
            passwordEncrypt,
            loginUrl,
            headers
        )
    except httpx.ConnectTimeout:
        pass
    except httpx.ConnectError:
        showMsg("连不上呢，你是不是没联网")
    except Exception as e:
        print(e)
        
def showMsg(msg,time:int=5):
    pass
    try:
        toast.show_toast(
        title="校园网连接服务",
        msg=msg,
        duration=time,
        icon_path=None,
        threaded=False
        )
    except TypeError :
        pass
def setNewUrl():
    res=httpx.get(oldUrl)
    match=re.search(r"href='(.*?)'",res.text)
    return match.group(1)


def setHeaders(newUrl):
    global headers
    res=httpx.get(newUrl)
    headers={
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "pragma": "no-cache",
            "sec-gpc": "1",
            "cookie": res.headers["Set-Cookie"],
            "Referer": newUrl,
            "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    return headers
def setQueryString(newUrl):
    match=re.search(r"\?(.*)",newUrl)
    queryString=match.group(1)
    return queryString

def setIp(newUrl):
    match=re.search(r"//([0-9\.]*?)/",newUrl)
    global ip
    ip=match.group(1)
    return ip

def setLoginUrl(loginUrl,ip):
    loginUrl=loginUrl.format(ip)
    return loginUrl

def login(
        userId,
        password,
        service,
        queryString,
        operatorPwd,
        operatorUserId,
        validcode,
        passwordEncrypt,
        loginUrl,
        headers,
):
    data={
        "userId":userId,
        "password":password,
        "service":service,
        "queryString":queryString,
        "operatorPwd":operatorPwd,
        "operatorUserId":operatorUserId,
        "validcode":validcode,
        "passwordEncrypt":passwordEncrypt,
    }
    res=httpx.post(loginUrl,data=data,headers=headers)
    res=res.json()
    if res["result"]=="success":
        showMsg("你成功的连上了校园网,ヽ(✿ﾟ▽ﾟ)ノ")
    elif res["result"]=="fail":
        showMsg(res["message"])
        quit()
showMsg("启动了，开始冲浪",1)
argus=sys.argv
userId=int(argus[1])
password=argus[2]
index=int(argus[3])
while True:
    main(userId,password,index)
    time.sleep(10)
