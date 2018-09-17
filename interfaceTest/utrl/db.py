import pymysql

from utrl.config import Config

host = Config().get ('HOST')
port=Config().get('PORT')
user=Config().get('user')
password=Config().get('password')
db=Config().get('db')
charset=Config().get('charset')
class Db:
    # connection = pymysql.connect (host='192.168.1.250', port=3306, user='dev_db_user', password='yrSuper001',
    #                               db='finance_hkjf',
    #                               charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    # cursor=connection.cursor()
    connection = pymysql.connect (host=host, port=port, user=user, password=password,db=db,charset=charset, cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor ()
