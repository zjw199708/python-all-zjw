from day16.untils.DBUntils import Mysqluntils
from day16.untils.Exceluntils import ExcelUntils

import os


class DataRead:
    list = None  # 全局列表 mode=excel，filename，sheetname

    # database：database ，user，password，tablename
    def __init__(self, mode, filename='', sheetname='0', host='localhost', database='', user='', password='',
                 tablename=''):
        if mode == 'excel':
            if filename == '':
                raise Exception('文件名不能为空！别瞎巴巴')
            elif not os.path.isfile(filename):
                raise Exception('文件不存在！别瞎巴巴')
            else:
                DataRead.list = ExcelUntils.read(filename, sheetname)

        elif mode == 'database':
            DataRead.list = Mysqluntils.read(host=host, database=database, user=user, password=password,
                                             tablename=tablename)
        else:
            raise Exception('对不起，您的操作模式无法识别')


d = DataRead('excel','D:\\python\\day16\\testcase\\qwer.xlsx','0')
print(d.list)


