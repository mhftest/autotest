# coding = utf-8

from urllib import request, parse
from urllib.error import URLError
import threading


class postRequest ():
    def __init__(self, url, values, interface_name):
        self.url = url
        self.values = values
        self.interface_name = interface_name

    def post(self):
        parms = self.values
        querystring = parse.urlencode (parms)
        try:
            u = request.urlopen (self.url, querystring.encode ('ascii'))
            resp = u.read ()
            print (u"接口名字为：", self.interface_name)
            print (u"所传递的参数为：\n", parms)
            print (u"服务器返回值为：\n", resp)
        except URLError as e:
            print (e)


def Login():  # 定义接口函数
    excel = DATA_PATH + '/test.csv'
    with open (excel, "r", encoding="utf-8") as f:
        reader = csv.reader (f)
        for col in reader:
            print (col)
            db = Db ()
            connection = db.connection
            cursor = db.cursor
            # cursor.execute ("SELECT message_note from sys_tel_message where tel='13301302026'")
            cursor.execute ("SELECT code from bidd_info where title='m季季81602'")
            connection.commit ()
            t = cursor.fetchall ()
            # a=t['tel']
            code = t[0]['code']
            print ('标的code:', code)
            tel = col
            print ('用户：', tel)
    # 实例化接口对象
    content = {'login': tel,
               'password': '2971055a690ad019e9fc08a9971080ccfd6a8b588c69acc28383a12d9cfdcb135a60550a4df643b9967c5fab90ce4eb8e3970c2c093fefe299662ac44e868763d281e8708ab625528d55c6a777b2700bcb9daf7e7e0c6805ffd13760d4ac0120d6f43c2dc05fc38fcff485eedd8859d79200ddb7a9a606b8548fa1d8def1dacc',
               'pwdLevel': '2', 'verify_code': '请输入计算结果', 'randCode': '请输入您的6位验证码',
               'commendPhone': '请输入推荐码(推荐人手机号后8位)',
               'loginregister': '请输入您的手机号', 'passwordresgister': '', 'token': '', 'modulus': '',
               'exponent': '', 'newToken': '', 'phoneId': '', 'code': '',
               'utype': '', 'csrftoken': '', 'pwdLevel': ''}
    # r = requests.post ('http://192.168.1.249:9901/hkjf/login.do?method=indexlogin',
    #                    data=content)  # 发送请求
    login = postRequest ('http://192.168.1.249:9901/hkjf/login.do?method=indexlogin', data=content)
    return login.post ()


try:
    i = 0
    tasks = []  # 任务列表
    task_number = 300
    while i < task_number:
        t = threading.Thread (target=Login)
        tasks.append (t)  # 加入线程池，按需使用
        t.start ()  # 多线程并发
except Exception as e:
    print (e)