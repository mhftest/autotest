import re
import time
import unittest
import paramunittest
import requests
from csh2 import getDir
from csh2.dxExcel import get_excel_value
from utrl.basepage import BasePage
from utrl.db import Db

proDir = getDir.proDir
now = time.strftime("%Y_%m_%d %H:%M:%S")
investCase = get_excel_value("bidInfoList.xls", "investCase")
# print(accountRecharge)
b=BasePage()
url1=b.get_url()
db=Db()
connection=db.connection
cursor=db.cursor
@paramunittest.parametrized(*investCase)
class InvestTest(unittest.TestCase):
    def setParameters(self,case_name,login,passwd,biddname,money,investRedPacketId,investRaiseInterestId):
        self.case_name = str(case_name)
        self.login = str(int(login))
        self.passwd = str(passwd)
        self.biddname=str(biddname)
        self.money = str(int(money))
        self.investRedPacketId = str(int(investRedPacketId))
        self.investRaiseInterestId = str(int(investRaiseInterestId))
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
        #http://192.168.1.249:8984/hk-financial-services/bidInfoController/invest.do
        url=url1+'/hk-financial-services/bidInfoController/invest.do'
        cursor.execute("SELECT id from bid_info where name=%s",self.biddname)
        connection.commit()
        t = cursor.fetchall ()
        print (t)
        bidid = t[0]['id']
        contentb={'bidId':bidid,'money':self.money,'investRedPacketId':self.investRedPacketId,'investRaiseInterestId':self.investRaiseInterestId}
        r2 = requests.post(url,data=contentb,cookies=c)  # 发送请求
        print ('status:', r2.status_code)
        t=r2.text
        print(t)
        resStatus = re.findall (r'<resStatus>(.+?)</resStatus>', t)
        print(resStatus)
        self.assertEqual(int(resStatus[0]), 1000)

        # dict=json.loads(text)
        # self.assertEqual (dict['errMsg'], self.excepted)
if __name__ == "__main__":
    unittest.main(verbosity=2)
#http://192.168.1.249:8984/hk-financial-services/withdrawCashController/clientWithDraw.do