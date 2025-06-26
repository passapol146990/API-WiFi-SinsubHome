import requests
import time
username = 115100
password = 2624
req = requests.session()
url = "http://172.16.0.1/portal/user-authen.php"
header = {
    "content-type":"application/x-www-form-urlencoded",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}
body = {
    "txtLogin":username,
    "txtPasswd":password,
    "btnLogin":"Login",
    "reqUrl":"https://www.google.com",
    "reqCheck":"false"
}


while True:
    response = req.get(url=url)
    isLogin = "You are currently online" in response.text
    print(time.strftime("%H:%M:%S", time.localtime()), username, password, "is Login : ", isLogin)
    if(not isLogin):
        req.post(url=url,headers=header,data=body)
    time.sleep(10)
