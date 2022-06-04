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
#可变参数
def f1(a,b,*c):
    print(a,b,c)
f1(2,3,4)

def f2(a,b,**c):
    print(a,b,c)
f2(2,3,name ='jiajia',age= '20')

def f3(a,b,*c,**d):
    print(a,b,c,d)
f3(1,2,39,20,name = 'jiajia',age = '20')

#强制命名参数
def f1(*a,b,c):
    print(a,b,c)

f1(2,b=3,c=4)
f1(2,3,4)
