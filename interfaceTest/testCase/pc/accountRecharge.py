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
accountRecharge = get_excel_value("pcloginCase.xls", "accountRecharge")
# print(accountRecharge)
b=BasePage()
url1=b.get_url()

@paramunittest.parametrized(*accountRecharge)
class AccountRechargeTest(unittest.TestCase):
    def setParameters(self, case_name, systemTypeName,platformSourceName,payChannel,payStyle,bankCode,bankCard,tiedCardFlag,transMoney,login,passwd):
        self.case_name = str(case_name)
        self.login = str(int(login))
        self.passwd = str(passwd)
        self.systemTypeName = str(systemTypeName)
        self.platformSourceName = str (platformSourceName)
        self.payStyle = str (payStyle)
        self.bankCode = str(bankCode)
        self.bankCard = str (bankCard)
        self.tiedCardFlag = str(int(tiedCardFlag))
        self.transMoney = str (transMoney)
        self.payChannel = str (payChannel)
    # def setUp(self):
    #     self.baseUrl = "http://www.mi.com"
    #     self.driver = webdriver.Chrome()
    #     self.driver.implicitly_wait(10)  # 静默等待10s

    def test_login(self):
        self._testMethodDoc = self.case_name  # 设置用例名称
        # 用户登录
        content = {'login': self.login,
                'passwd': self.passwd}
        #http://192.168.1.249:8984/hk-financial-services/indexController/fasterLogin.do
        url=url1+'/hk-financial-services/indexController/fasterLogin.do'
        r = requests.post (url,data=content)  # 发送请求
        print ('status:', r.status_code)
        t=r.text
        c=r.cookies
        #http://192.168.1.249:8984/hk-financial-services/indexController/fasterLogin.do
        url=url1+'/hk-financial-services/finPaymentRechargeController/accountRecharge.do'
        contentcar={'systemTypeName':self.systemTypeName,
                    'platformSourceName':self.platformSourceName,
                    'payChannel':self.payChannel,
                    'payStyle':self.payStyle,
                    'bankCode':self.bankCode,
                    'bankCard':self.bankCard,
                    'tiedCardFlag':self.tiedCardFlag,
                    'transMoney':self.transMoney}
        r2 = requests.post(url,data=contentcar,cookies=c)  # 发送请求
        print ('status:', r2.status_code)
        t=r2.text
        print(t)
        resStatus = re.findall (r'<resStatus>(.+?)</resStatus>', t)
        print(resStatus[0])
        self.assertEqual(int(resStatus[0]), 1000)

        # dict=json.loads(text)
        # self.assertEqual (dict['errMsg'], self.excepted)
if __name__ == "__main__":
    unittest.main(verbosity=2)
#http:http://192.168.1.249:8984/hk-financial-services/finPaymentRechargeController/accountRecharge.do