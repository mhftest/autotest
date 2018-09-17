import os
import requests
from PIL import Image
from io import BytesIO
# a='abcdefg'
# print(a[:3])
# print(a[3:])
#r = requests.get('https://www.baidu.com')
# response=requests.get("https://api.github.com/events")
r=requests.get("https://www.hongkunjinfu.com")
r.encoding = 'utf-8'
# print(r.text)
# print(r.status_code)
# print(r.encoding)
# print(r.content)#二进制响应内容
# i=Image.open(BytesIO(r.content))
info = r.json()

print(info)
print(info[0]['id'])
token = info[0]['id']
# logger.debug("Create token:%s" % (token))
# return token
print(token)

# import paramunittest   in  testLogin