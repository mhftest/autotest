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
print(url1)
proDir = getDir.proDir
now = time.strftime("%Y_%m_%d %H:%M:%S")
getyzmCase = get_excel_value("getYZM.xls", "getYZM_test")
print(getyzmCase)

@paramunittest.parametrized(*getyzmCase)
class getYZMTest(unittest.TestCase):
    def setParameters(self, case_name, access_token, imgyzm, mobile, type,excepted):
        self.case_name = str(case_name)
        self.access_token = str(access_token)
        self.imgyzm = str(imgyzm)
        self.mobile = str(mobile)
        self.type = str(type)
        self.excepted = str (excepted)
      # def setUp(self):
    #     self.baseUrl = "http://www.mi.com"
    #     self.driver = webdriver.Chrome()
    #     self.driver.implicitly_wait(10)  # 静默等待10s
    def test_login(self):
        self._testMethodDoc = self.case_name  # 设置用例名称
        # 用户登录
        content = {'access_token': self.access_token,
                'imgyzm': self.imgyzm,
                'mobile': self.mobile,
                'type': self.type}
        #拼接接口请求地址 # http://192.168.1.249:9921/hkjfapp/regist/getRegistVerifyCodeWithYzm
        url=url1+'/regist/getRegistVerifyCodeWithYzm'
        r = requests.post (url,data=content)  # 发送请求
        print ('status:', r.status_code)
        print (r.text)
        # self.assertEqual(errMsg, self.excepted)
        text=r.text
        dict=json.loads(text)
        # self.assertEqual (dict['errMsg'], self.excepted)
if __name__ == "__main__":
    unittest.main(verbosity=2)