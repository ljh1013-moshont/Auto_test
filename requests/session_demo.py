import requests

session =requests.Session()

session.headers.update({
    "User-Agent":"AutoTest/1.0",
    "Accept":"application/json",
    "Content-Type":"application/json"
})

login_resp = session.post(
    "https://api.example.com/login",
    json={"username":"admin","password":"123456"}
)
print("登录状态：",login_resp.json())

profile_resp =session.get("https://api.example.com/user/profile")
print("用户信息",profile_resp.json())


session.post("https://api.example.com/logout")

session.close()