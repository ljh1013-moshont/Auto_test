#requests基本语法
import requests
from requests import post

response =requests.get("https://httpbin.org/get")
print(response.status_code)
print(response.json())

params ={"key":"value","page":1,"size":20}
response =requests.get("https://httpbin.org/post",params=params)
print(response.url)

headers ={"User-Agent":"MyTestClient/1.0","Accept":"application/json"}
response=requests.get("https://httpbin.org/get",headers=headers)

data={"username":"admin","password":"123456"}
response=requests.post("https://httpbin.org/post",data=data)

json_data={"username":"admin","password":"123456"}

response=requests,post("https://httpbin.org/post",json=json_data)
#整体更新资源
response=requests.put("https://httpbin.org/put",json={"name":"updated"})

response=requests.delete("https://httpbin.org/delete")

#局部更新资源
response=requests.patch("https://httpbin.org/patch",json={"field":"value"})

response=requests.get("https://httpbin.org/get")

print(response.status_code)       #状态码
print(response.headers)           #响应头
print(response.text)              #响应码文本
print(response.json())            #响应体json解析
print(response.content)           #响应体字节流
print(response.encoding)          #响应编码
print(response.elapsed.total_seconds())    #请求耗时

