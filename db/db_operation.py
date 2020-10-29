import pymysql


class DbOperation:
    def __init__(self, host='172.17.4.234', user='liran', password='123456', database='crm', port=3306, charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset

    def open(self):
        # 创建连接
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port,
                                    database=self.database, charset='utf8')
        # 创建游标
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def search_info(self, sql):
        self.open()
        try:
            # sql = 'select * from tb_user where username="111111111"'
            # 执行sql
            self.cur.execute(sql)
            # fetchall()方法获取数据
            res = self.cur.fetchall()
            return res
        except Exception as e:
            print('sql execute failed')
            self.conn.rollback()
        finally:
            self.close_cursor_and_conn()

    def update_operation(self, sql):
        self.open()
        try:
            # sql = 'update tb_user set grade = "1" where username="111111111"'
            # 执行sql
            self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            print('sql execute failed')
            self.conn.rollback()
        finally:
            self.close_cursor_and_conn()

    def delete_info(self, sql):
        self.open()
        try:
            # sql = 'delete from tb_user where username="2222"'
            # 执行sql
            self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            print('sql execute failed')
            self.conn.rollback()
        finally:
            self.close_cursor_and_conn()

    def close_cursor_and_conn(self):
        # 关闭游标
        self.cur.close()
        # 关闭链接
        self.conn.close()
