"""mysql"""
import pymysql
from pymysql.cursors import DictCursor

IP = '47.93.23.130'
USER = 'zad'
PASSWORD = '123158'
DATABASE = 'note'

class Mysql():
    """mysql DAO"""
    def __init__(self, conn):
        self.conn = conn

    def connect(self):
        """连接数据库"""
        self.conn = pymysql.connect(IP, USER, PASSWORD, DATABASE)
    
    def disconnect(self):
        """与数据库断开连接"""
        self.conn.close()

    def execute_sql(self, sql):
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
            cursor.close()
        except BaseException:
            self.conn.rollback()

    def execute_query(self, sql):
        print('execute sql:' + sql)
        cursor = self.conn.cursor(DictCursor)
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows
