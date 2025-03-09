import requests as req
username = 151023
password = 3314

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
reqs = req.session()
res = reqs.post(url=url,headers=header,data=body)
print(res.text)
print("Login successfully" in res.text)
