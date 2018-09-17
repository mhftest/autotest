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
print('获取目录：',proDir)
now = time.strftime("%Y_%m_%d %H:%M:%S")
authCase = get_excel_value("auth.xls", "auth_test")
print(authCase)

@paramunittest.parametrized(*authCase)
class AuthTest(unittest.TestCase):
    def setParameters(self, case_name, client_id, client_secret, grant_type, password,scope,username):
        self.case_name = str(case_name)
        self.client_id = str(client_id)
        self.client_secret = str(client_secret)
        self.grant_type = str(grant_type)
        self.password = str(password)
        self.scope = str(scope)
        self.username = str(username)
    def test_login(self):
        self._testMethodDoc = self.case_name  # 设置用例名称
        # 用户登录
        content = {'client_id': self.client_id,
                'client_secret': self.client_secret,
                'grant_type': self.grant_type,
                'password': self.password,
                'scope': self.scope,
                'username': self.username}
        #拼接接口请求地址
        url=url1+'/oauth/token'
        r = requests.post (url,data=content)  # 发送请求
        print ('status:', r.status_code)
        print (r.text)
        # self.assertEqual(errMsg, self.excepted)
        text=r.text
        dict=json.loads(text)
        # self.assertEqual (dict['errMsg'], self.excepted)
if __name__ == "__main__":
    unittest.main(verbosity=2)