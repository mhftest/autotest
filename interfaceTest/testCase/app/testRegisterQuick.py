import readConfig as readConfig
import unittest
import paramunittest
from utrl.Log import MyLog
from utrl import configHttp
from utrl import common_1
from utrl import configDB

localRegisterQuick_xls = common_1.get_xls("userCase.xlsx", "registerquick")
localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()
localConfigDB = configDB.MyDB()


@paramunittest.parametrized(*localRegisterQuick_xls)
class RegisterQuick(unittest.TestCase):

    def setParameters(self, case_name, method, token, email, result, code, msg):
        """
        set parameters
        :param case_name:
        :param method:
        :param token:
        :param email:
        :param result:
        :param code:
        :param msg:
        :return:
        """
        self.case_name = str(case_name)
        self.method = str(method)
        self.token = str(token)
        self.email = str(email)
        self.result = str(result)
        self.code = str(code)
        self.msg = str(msg)
        self.response = None
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
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()

    def testRegisterQuick(self):
        """
        test body
        :return:
        """
        # set url
        self.url = common_1.get_url_from_xml('registerQuick')
        localConfigHttp.set_url(self.url)

        # set header
        if self.token == '0':
            token = localReadConfig.get_headers("token_v")
        elif self.token == '1':
            token = None
        header = {'token': token}
        localConfigHttp.set_headers(header)

        # set params
        data = {'email': self.email}
        localConfigHttp.set_data(data)

        # test interface
        self.response = localConfigHttp.post()

        # check result
        self.checkResult()

    def tearDown(self):
        """

        :return:
        """
        self.log.build_case_line(self.case_name, self.info['code'], self.info['msg'])

    def checkResult(self):
        """

        :return:
        """
        self.info = self.response.json()
        common_1.show_return_msg(self.response)

        if self.result == '0':
            email = common_1.get_value_from_return_json(self.info, 'member', 'email')
            self.assertEqual(self.info['code'], self.code)
            self.assertEqual(self.info['msg'], self.msg)
            self.assertEqual(email, self.email)

        if self.result == '1':
            self.assertEqual(self.info['code'], self.code)
            self.assertEqual(self.info['msg'], self.msg)
            if self.case_name == 'registerQuick_EmailExist':
                sql = common_1.get_sql('newsitetest', 'rs_member', 'delete_user')
                localConfigDB.executeSQL(sql, self.email)
                localConfigDB.closeDB()
