'''
将老师随机分配到不同的办公室
'''

import random
# 定义一个列表用来保存3个办公室
offices = [[],[],[]]
# 定义一个列表用来存储8位老师的名字
names = ['王重阳','黄药师','杨过','郭靖','张三丰','乔峰','张无忌','洪七公']
i = 0
for name in names:
   index = random.randint(0,2) # 行索引
   offices[index].append(name)
i = 1 # 办公室编号
for tempNames in offices:
   print('办公室%d的人数为:%d'%(i,len(tempNames)))
   i+=1
   for name in tempNames:
        print("%s、 "%name,end='')
   print("-"*20)