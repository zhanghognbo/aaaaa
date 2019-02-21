# 生成字典的四种方式
# d1=dict({"id":1948,"name":"Washer","size":3})
# d2=dict(id=1948,name="Washer",size=3)
# d3=dict([("id",1948),("name","Washer"),("size",3)])
# d4={"id":1948,"name":"Washer","size":3}
#
# print(d1)
# print(d2)
# print(d3)
# print(d4)
# print(len(range(1,10)))
# print(set([1,2,3])=={1,2,3})
# true
# print([1]+[4])
# [l,4]
# 用while循环求阶乘
# i=1
# n=(int(input("请输入一个数：")))
# jie=1
# sum=0
# while n>=i:
#     jie=jie*i
#     sum+=jie
#     i+=1
# print(sum)
# 1.有一列分数序列，2／1，3／2，5／3，8／5。。。求出前20项之和
# n=int(input('请输入项数：'))
# fenzi=2
# fenmu=1
# l=[]
# s=0
# for i in range(1,n+1):
#     a=fenzi
#     b=fenmu
#
#     s+=(a/b)
#     l.append('%s/%s'%(a,b))
#
#     fenzi=a+b
#     fenmu=a
# print('+'.join(str(i) for i in l),end='')
# print('=%.2f'%s)
# 用for循环求分数数列和
# fenzi=2
# fenmu=1
# sum=0
# for i in range(1,21):
#     sum+=fenzi/fenmu
#     t=fenzi
#     fenzi=fenzi+fenmu
#     fenmu=t
# print(sum)
# 3.有四个数字1，2，3，4，能组成多少个互不相同的三位数
# if __name__=="__main__":
#     count=0
#     for i in range(1,5):
#         for j in range(1,5):
#             for k in range(1,5):
#                 if i!=j and i!=k and j!=k:
#                     print(i,j,k)
#                     count+=1
#     print("能组成{}个互不重复的三位数：".format(count))
# 4.实现100-200里面所有的质数字,打印这些质数并且求出个数
# 优化三位数打印不重复
# for x in range(1,5):
#     for y in range(1,5):
#         for z in range(1,5):
#                 if (x!=y) and (y!=z) and (z!=x):
#                     i += 1
#                     if i%4:
#                         print("%d%d%d" % (x, y, z), end=" | ")
#                     else:
#                         print("%d%d%d" % (x, y, z))
#coding=utf-8
#函数用于判断某一个数是不是素数

def test(num):
    list = [] #定义列表，用于存储计算
    i = num -1#去除本身
    while i > 1:#去除1
        if num%i == 0: #判断是否有余数
            list.append(i)#将所以有的能整除它数加入列表
        i -= 1
    if len(list) == 0:#如果列表为空，就是表示除了1个它本身能整除
        print(num,end=" ")
#此函数用于判断计算出需要判断的所有数字100～200
def test2(star_num,and_num):
    j = star_num
    while j < and_num:
        test(j)
        j += 1
test2(100,200)

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%s*%s=%s"%(j,i,i*j),end='  ')
#     print()

