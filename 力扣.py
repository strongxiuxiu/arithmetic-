database_info = {
    "self_databases": ("192.168.4.111", 'root', 1433, 'password', "dbname"),
    # 总公司sql server 查询数据  # ip  ,user,   端口     ,密码 ,    数据库名称
    "HC01server": ("192.168.4.111", 'root', 1433, 'password', "dbname"),
    "HC02server": ("192.168.4.111", 'root', 1433, 'password', "dbname"),
    "HC03server": ("192.168.4.111", 'root', 1433, 'password', "dbname"),
    "HC04server": ("192.168.4.111", 'root', 1433, 'password', "dbname"),
    "HC05server": ("192.168.4.111", 'root', 1433, 'password', "dbname"),
    "HC06server": ("192.168.4.111", 'root', 1433, 'password', "dbname"),
    "HC07server": ("192.168.4.111", 'root', 1433, 'password', "dbname"),
    "HC08server": ("192.168.4.111", 'root', 1433, 'password', "dbname"),
    "HC09server": ("192.168.4.111", 'root', 1433, 'password', "dbname"),

}

import pymssql


class DBHelper:
    def __init__(self, host="127.0.0.1", port="1433", user="sa", password="123456", database="test", company_name=None):
        try:
            self.conn = pymssql.connect(host, user, password, database)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)
        self.company_name = company_name

    def __repr__(self):
        return self.company_name

    # 返回执行execute()方法后影响的行数
    def execute(self, HC63sql_path):
        HC63sql_path = r'C:\br_status\Shoptotalcount.sql'
        HC63sql = open(HC63sql_path, 'r', encoding="utf-8-sig")
        sqltxt = HC63sql.readlines()
        self.cursor.execute(sqltxt)
        rowcount = self.cursor.rowcount
        return rowcount

    def __del__(self):
        '''free source.'''
        try:
            self.conn.close()
            self.cursor.close()
        except:
            pass


if __name__ == '__main__':
    for key, values in database_info.items():
        db_object = {}
        db_object[key] = DBHelper(host=values[0], port=values[1], user=values[2], password=values[3],
                                  database=values[4])
        for i, j in db_object.items():
            # i = 公司名称  j =公司对象
            if i == "某公司":
                res = j.execute('sql')