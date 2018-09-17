#-*- coding:utf-8 -*-
import hashlib
import unittest
import time
import sys
import re
import requests
from testjf1.common.db import Db
from testjf1.common.loginpage import LoginPage
from testjf1.interface.test3 import Mysign
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
from utils.jiami import Sign

sys.path.append('D:\\jftest1_CG\\test1')
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class Test_duoren_invest(unittest.TestCase):
    excel = DATA_PATH + '/register.xlsx'
    def test_Login(self):
        # excel = DATA_PATH + '/register.xlsx'
        datas = ExcelReader (self.excel).data
        db = Db ()
        connection = db.connection
        cursor = db.cursor
        for d in datas:
            with self.subTest (data=d):
                cursor.execute ("SELECT code from bidd_info where title='我推荐啊啊'")
                connection.commit ()
                t = cursor.fetchall ()
                # a=t['tel']
                code = t[0]['code']
                print ('标的code:', code)
                tel=int(float(d['title']))
                print('用户：',tel)
                # 用户登录
                content = {'access_token':'1b1d5757-9322-4d83-bb79-fed79f973dad','mobileUDID': '2cae768b2925730a','password': 'MD9680KzfSP2FwvHIdHs5EsjGCimsJVmZ0r2oNpitRMOldTDyoPkLNpr2DonPkf64uQRc7iayzYGMmk1SR6Cyvm2lqluLLhIcnZi8Y8+aYp4mtZwJjGhoc20yCdWlcmhAfWB/WnxHVoyYeNReeJUkUprnfR8K0MZ5Hmwik4lm/w=',
                           'appVersion': 'v2.6.3', 'mobileModel': 'MI 4LTE','login':tel,'mobileVersion': '6.0.1','mobileIp': '02:00:00:00:00:00','mobileMAC': '02:00:00:00:00:00','passLength': '6',}
                r = requests.post ('http://192.168.1.249:9921/hkjfapp/user/doLogin',data=content)  # 发送请求
                print ('登录响应状态', r.status_code)
                txt=r.text
                print(r.text)
                c = r.cookies
                # r = re.findall (r'<input name="token"  type="hidden"  value="(.+?)"/>', txt)
                usercode=re.findall(r'资","code":"(.+?)","gender":"',txt)
                sessionid=re.findall(r',"sessionId":"(.+?)","userType',txt)
                print(usercode,'   ',sessionid)
                # 投标
                content_tz = { 'amount': '1000',
                              'biddCode': code,
                              'investType': '1',
                              'sessionId': sessionid[0],
                              'signType': 'MD5',
                              'source': '4',
                              'userCode': usercode[0]
                              }
                #描述 用户对标的进行指定金额的投资接口 签名生成方式，key保证a-z有序并且组装成URL请求形式，使用RSA生成签名，sign和空值key不参与组装，当使用md5签名时，将MD5秘钥加在原串的最后 &key=******
                # URL1 = "http://192.168.1.249:9921/hkjfapp/invest/invest?"
                a = Mysign.mysign (content_tz)
                print(a)
                a1=a+'&key=AMvFWdickzxK/sCwiG5BVKu8HkqxcrQEjSKmvCfZ44QfNsKiV7pG1'
                print(a1)
                m = hashlib.md5 ()  # 创建md5对象
                m.update (a1.encode (encoding='UTF-8'))  # 生成加密串，其中password是要加密的字符串
                # hashlib.md5('abcdefg'.encode(encoding='UTF-8')).hexdigest()
                sign = m.hexdigest ()
                print (sign)
                # # urlll=a+'&sign='+sign
                # # print(urlll)
                content_tz2 = {'access_token': '1b1d5757-9322-4d83-bb79-fed79f973dad',
                              'amount': '1000',
                              'biddCode': code,
                              'investType': '1',
                              'sessionId': sessionid[0],
                               'sign':sign,
                              'signType': 'MD5',
                              'source': '4',
                              'userCode': usercode[0]
                              }
                rtz = requests.post ("http://192.168.1.249:9921/hkjfapp/invest/invest",params=content_tz2,cookies=c)
                print('投资状态',rtz.status_code)
                print(rtz.text)
if __name__ == '__main__':
    unittest.main ()