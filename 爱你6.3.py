print("ainiya 佳佳")
#局部变量和全局变量的效率测试
import math
import time

def test():   #用的是全局变量
    start = time.time()
    for i in range(10000000):
        math.sqrt(30)
    end = time.time()
    print("耗费时间{0}".format((end - start)))

def test01():
    b = math.sqrt#用b引用模块，使用局部变量
    start = time.time()
    for i in range (10000000):
        b(30)
    end = time.time()
    print("耗时{0}".format((end  - start)))
test()
test01()
