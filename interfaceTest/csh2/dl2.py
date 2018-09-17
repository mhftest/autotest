import json
import os
import time
import unittest
from time import sleep
import paramunittest
import requests
from selenium import webdriver
from csh import getDir
from csh.dxExcel import get_excel_value
proDir = getDir.proDir
now = time.strftime("%Y_%m_%d %H:%M:%S")
loginCase2 = get_excel_value("loginCase2.xls", "login_test2")
print(loginCase2)

@paramunittest.parametrized(*loginCase2)
class LoginTest(unittest.TestCase):
    def setParameters(self, case_name, login, password, pwdLevel, verify_code,randCode,commendPhone, loginregister,passwordresgister,
                      token,modulus,exponent,newToken,phoneId,code,utype,csrftoken,excepted):
        self.case_name = str(case_name)
        self.verify_code = str(verify_code)
        self.login = str(login)
        self.password = str(password)
        self.pwdLevel = str(pwdLevel)
        self.commendPhone = str(commendPhone)
        self.loginregister = str(loginregister)
        self.randCode = str(randCode)
        self.passwordresgister = str (passwordresgister)
        self.token = str (token)
        self.modulus = str (modulus)
        self.exponent = str (exponent)
        self.newToken = str (newToken)
        self.code = str (code)
        self.utype = str (utype)
        self.phoneId = str (phoneId)
        self.csrftoken = str (csrftoken)
        self.excepted = str(excepted)

    # def setUp(self):
    #     self.baseUrl = "http://www.mi.com"
    #     self.driver = webdriver.Chrome()
    #     self.driver.implicitly_wait(10)  # 静默等待10s

    def test_login(self):
        self._testMethodDoc = self.case_name  # 设置用例名称
        # 用户登录
        content = {'login': self.login,
                'password': self.password,
                'pwdLevel': self.pwdLevel, 'verify_code': self.verify_code, 'randCode': self.randCode,
                'commendPhone': self.commendPhone,
                'loginregister': self.loginregister, 'passwordresgister': self.passwordresgister, 'token': self.token,
                'modulus': self.modulus,
                'exponent': self.exponent, 'newToken': self.newToken, 'phoneId': self.phoneId, 'code': self.code,
                'utype': self.utype, 'csrftoken': self.csrftoken, 'pwdLevel': self.pwdLevel}
        r = requests.post ('http://192.168.1.249:9901/hkjf/login.do?method=indexlogin',
                           data=content)  # 发送请求
        # print ('status:', r.status_code)
        # print (r.text)
        # self.assertEqual(errMsg, self.excepted)
        text=r.text
        dict=json.loads(text)
        self.assertEqual (dict['errMsg'], self.excepted)
if __name__ == "__main__":
    unittest.main(verbosity=2)