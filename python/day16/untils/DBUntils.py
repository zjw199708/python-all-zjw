import pymysql


class Mysqluntils:
    con = None
    cursor = None

    @classmethod
    def read(cls, host='localhost', database='student', user='root'
             , password='', tablename='choose'):
        cls.con = pymysql.connect(host=host, user=user, password=password,
                                  database=database, charset='utf8')
        cls.cursor = cls.con.cursor()

        sql = '''
        select * from {tablename}
        '''
        cls.cursor.execute(sql.format(tablename=tablename))
        return cls.cursor.fetchall()

# s= Mysqluntils.read()
# print(s)