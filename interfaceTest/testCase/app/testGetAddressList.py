import unittest
import paramunittest
import readConfig as readConfig
from utrl import Log as Log
from utrl import common_1
from utrl import configHttp as ConfigHttp
from utrl import businessCommon

addressList_xls = common_1.get_xls("userCase.xlsx", "getAddressList")
localReadConfig = readConfig.ReadConfig()
configHttp = ConfigHttp.ConfigHttp()
info = {}


@paramunittest.parametrized(*addressList_xls)
class GetAddressList(unittest.TestCase):
    def setParameters(self, case_name, method, token, result, code, msg):
        """
        set params
        :param case_name:
        :param method:
        :param token:
        :param result:
        :param code:
        :param msg:
        :return:
        """
        self.case_name = str(case_name)
        self.method = str(method)
        self.token = str(token)
        self.result = str(result)
        self.code = str(code)
        self.msg = str(msg)
        self.info = None

    def description(self):
        """

        :return:
        """
        self.case_name

    def setUp(self):
        """

        :return:
        """
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()
        self.login_token = businessCommon.login()

    def testGetAddressList(self):
        """
        test body
        :return:
        """
        # set url
        self.url = common_1.get_url_from_xml('getAddressList')
        configHttp.set_url(self.url)
        print(self.url)

        # get token
        if self.token == '0':
            token = self.login_token
        else:
            token = self.token

        # set headers
        header = {"token": str(token)}
        configHttp.set_headers(header)

        # test interface
        self.return_json = configHttp.get()

        # check result
        self.checkResult()

    def tearDown(self):
        """

        :return:
        """
        businessCommon.logout(self.login_token)
        self.log.build_case_line(self.case_name, self.info['code'], self.info['msg'])

    def checkResult(self):
        """
        check test result
        :return:
        """
        self.info = self.return_json.json()
        common_1.show_return_msg(self.return_json)

        if self.result == '0':
            self.assertEqual(self.info['code'], self.code)
            self.assertEqual(self.info['msg'], self.msg)
            self.assertIsNotNone(self.info['info']['address'])

        if self.result == '1':
            self.assertEqual(self.info['code'], self.code)
            self.assertEqual(self.info['msg'], self.msg)
