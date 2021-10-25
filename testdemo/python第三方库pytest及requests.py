import requests

# get请求
r=requests.get("http://www.baidu.com")
# 返回值状态码
print(r.status_code)  # 输出200 请求成功标识

# 编码
print(r.encoding) # 输出：ISO-8859-1
r.encoding="utf-8"
print(r.encoding)  # 输出：utf-8

# 输出文本信息
print(r.text)

print("-----------post请求-------------")
# post请求
rpost=requests.post('http://httpbin.org/post',data={'key':'value'})
print(rpost.text)
#  输出
"""
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "key": "value"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "9", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.22.0", 
    "X-Amzn-Trace-Id": "Root=1-6170ee3e-413a27585628a9c243f12fee"
  }, 
  "json": null, 
  "origin": "101.33.125.232", 
  "url": "http://httpbin.org/post"
}
"""