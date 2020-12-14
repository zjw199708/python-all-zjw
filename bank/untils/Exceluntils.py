import xlrd

class ExcelUntils:
    @classmethod
    def read(cls,filename='',sheetname = '0'):
        try:
            list = []
            file = xlrd.open_workbook(filename,)
            if sheetname.isdigit():#如果给的选项卡是数字
                sheet = file.sheet_by_index(int(sheetname))
                #获取所有行
                rows = sheet.nrows
                for i in range(rows):
                    list.append(sheet.row_values(i))
                return list
            else:
                sheet = file.sheet_by_name(sheetname)
                rows = sheet.nrows
                for i in range(rows):
                    list.append(sheet.row_values(i))
                return list
        except Exception as error:
            print(error)


# s = ExcelUntils.read('D:\\python\\day16\\testcase\\qwer.xlsx','0')
# print(s)