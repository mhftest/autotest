import json
import re
import time
import unittest
import paramunittest
import requests
from csh2 import getDir
from csh2.dxExcel import get_excel_value
from utrl.basepage import BasePage

proDir = getDir.proDir
now = time.strftime("%Y_%m_%d %H:%M:%S")
testsearchInfomation = get_excel_value("pcloginCase.xls", "searchInfomation_test")
# print(testsearchInfomation)
b=BasePage()
url1=b.get_url()

@paramunittest.parametrized(*testsearchInfomation)
class SearchInfomation_Test(unittest.TestCase):
    def setParameters(self, case_name, type, channel,position):
        self.case_name = str(case_name)
        self.type = str(int(type))
        self.channel = str(int(channel))
        self.position = str(int(position))
    def test_login(self):
        self._testMethodDoc = self.case_name  # 设置用例名称
        # 用户登录
        content = {'type': self.type, 'channel': self.channel,   'position': self.position}
        #http://192.168.1.249:8984/hk-financial-services/indexController/fasterLogin.do
        url=url1+'/hk-financial-services/informationController/searchInfomation.do'
        r = requests.post (url,data=content)  # 发送请求
        print ('status:', r.status_code)
        t=r.text
        print(t)
        resStatus = re.findall (r'<resStatus>(.+?)</resStatus>', t)
        print(resStatus[0])
        self.assertEqual(int(resStatus[0]), 1000)

        # dict=json.loads(text)
        # self.assertEqual (dict['errMsg'], self.excepted)
if __name__ == "__main__":
    unittest.main(verbosity=2)
# http://192.168.1.249:8984/hk-financial-services/informationController/searchInfomation.do