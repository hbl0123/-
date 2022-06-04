print("aini jiajia")
#测位置参数
def f1(a,b,c):
    print(a,b,c)
f1(1,2,3,)
f1(2,3,3)
#默认值参数
def f1(a,b,c=10,d=40):
    print(a,b,c,d)
f1(1,3,5)
f1(3,4)
#命名参数
def f1(a,b,c):
    print(a,b,c)
f1(8,9,10)
f1(b=10,a=30,c=59)
