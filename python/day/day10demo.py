import xlrd

# 1. 打开工作簿并获取句柄
data = xlrd.open_workbook('D:\\python\\day\\a.xlsx')
# 2.从工作簿里选中选项卡
sheet = data.sheet_by_name('用户管理')

print('有{}行数据，有{}列数据'.format(sheet.nrows, sheet.ncols))

rows = sheet.nrows  # 获取行数据
cols = sheet.ncols  # 获取列数据

f = open('用户管理.txt', 'w', encoding='utf-8')
for i in range(rows):
    a = []
    for j in range(cols):
        a.append(str(sheet.cell_value(i, j)).replace('.0', ''))
    string = ','.join(a)  # 将 ，插入到列表中 '张三，56，男，12465132'
    f.write(string + '\n')
f.close()
