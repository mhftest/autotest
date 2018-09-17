import unittest
import paramunittest
import time

@paramunittest.parametrized(
    {"user": "admin", "psw": "123", "result": "true"},
    {"user": "admin1", "psw": "1234", "result": "true"},
    {"user": "admin2", "psw": "1234", "result": "true"},
    {"user": "admin3", "psw": "1234", "result": "true"},
    {"user": "admin4", "psw": "1234", "result": "true"},
    {"user": "admin5", "psw": "1234", "result": "true"},

)

class TestDemo(unittest.TestCase):
    def setParameters(self, user, psw, result):
        '''这里注意了，user, psw, result三个参数和前面定义的字典一一对应'''
        self.user = user
        self.psw = psw
        self.result = result

    def testcase(self):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        print("输入用户名：%s" % self.user)
        print("输入密码：%s" % self.psw)
        print("期望结果：%s " % self.result)
        time.sleep(0.5)
        self.assertTrue(self.result == "true")

if __name__ == "__main__":
    unittest.main(verbosity=2)
#
# 4.注意了，这里的执行顺序是先执行0，1，再执行10，11，12依次来的，别问我为什么，也别找我解决，设计如此，之前ddt框架也是有同样的问题。
#
# 5.除了传字典参数，传元组类型的也是可以的
#
# @paramunittest.parametrized(
#     ("admin", "123", "true"),
#     ("admin1", "123", "true"),
#     ("admin2", "123", "true"),
#     ("admin3", "123", "true"),
#     ("admin4", "123", "true"),
#     ("admin5", "123", "true"),
#     ("admin6", "123", "true"),
#     ("admin7", "123", "true"),
#     ("admin8", "123", "true"),
#     ("admin9", "123", "true"),
#     ("admin10", "123", "true"),
#     ("admin11", "123", "true"),
#     ("admin12", "123", "true")
# )