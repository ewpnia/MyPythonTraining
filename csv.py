# -*- coding: utf-8 -*-

import csv

with open('csv_test.csv', 'wb') as f:
     writer = csv.writer(f)
# csvfile = file('csv_test.csv', 'wb')
# writer = csv.writer(csvfile)

writer.writerows(['序号', '姓名', '性别', '年龄', '电话',])

datas = [('小怪兽', '女', '36669', '123456'),
        ('奥特曼', '男', '36668', '123456'),
        ('刚大木', '男', '17', '789456123'),
        ('扎古', '男', '25', '987654321'),
        ('星光体', '不明', '不明', '不明'),]

for (no, data) in range(0, 5), datas:
    writer.writerows([no, data])

csvfile.close()



# import csv
# with open('some.csv', 'rb') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print row


# with open('passwd', 'rb') as f:
#     reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
#     for row in reader:
#         print row


# with open('some.csv', 'wb') as f:
#     writer = csv.writer(f)
#     writer.writerows(someiterable)

# import csv
# for row in csv.reader(['one,two,three']):
#     print row