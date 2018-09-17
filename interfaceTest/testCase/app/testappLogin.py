#!/usr/bin/env python
#-*-coding:utf-8-*-
import json
import time
import unittest
import paramunittest
import requests
from csh2 import getDir
from csh2.dxExcel import get_excel_value
from utrl.basepage import BasePage

b=BasePage()
url1=b.get_url()
# print(url1)
now = time.strftime("%Y_%m_%d %H:%M:%S")
applogin22 = get_excel_value("applogin2.xls", "applogin2_test")
# print(applogin22)

@paramunittest.parametrized(*applogin22)
class apploginTest(unittest.TestCase):
    def setParameters(self, case_name,access_token, appVersion, login, mobileIp,mobileMAC, mobileModel, mobileUDID, mobileVersion,passLength, password,excepted):
        self.case_name = str(case_name)
        self.access_token = str(access_token)
        self.appVersion = str(appVersion)
        self.login = str(int(login))
        self.mobileIp = str(mobileIp)
        self.mobileMAC=str(mobileMAC)
        self.mobileModel=str(mobileModel)
        self.mobileUDID=str(mobileUDID)
        self.mobileVersion=str(mobileVersion)
        self.passLength=str(int(passLength))
        self.password=str(password)
        self.excepted=str(excepted)
            # def setUp(self):
    #     self.baseUrl = "http://www.mi.com"
    #     self.driver = webdriver.Chrome()
    #     self.driver.implicitly_wait(10)  # 静默等待10s
    def test_applogin(self):
        self._testMethodDoc = self.case_name  # 设置用例名称
        # 用户登录
        content = {'access_token': self.access_token,
                'passLength': self.passLength,
                'mobileIp': self.mobileIp,
                'password': self.password,
                'appVersion': self.appVersion,
                'mobileModel': self.mobileModel,
                'mobileVersion': self.mobileVersion,
                'mobileUDID': self.mobileUDID,
                'mobileMAC': self.mobileMAC,
                'login': self.login}
        print(content)
        #拼接接口请求地址 # http://192.168.1.249:9921/hkjfapp/user/doLogin   https://www.hongkunjinfu.com/hkjfapp/user/doLogin
        url=url1+'/user/doLogin'
        # print(url)      #   http://192.168.1.249:9921/hkjfapp/user/doLogin
        # r = requests.post (url,data=json.dumps(content))  # 发送请求
        r = requests.post(url, data=content)
        print ('status:', r.status_code)
        print (r.text)
        dict = json.loads(r.text)
        self.assertEqual (dict['msg'], self.excepted)
if __name__ == "__main__":
    unittest.main(verbosity=2)