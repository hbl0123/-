print("aini jiajia")

def outer():
    b= 10
    def inner():
        nonlocal b          #声明外部函数的局部变量
        print("inner:",b)
        b=20
        global a #声明全局变量
        a = 1000
    inner()
    print("outer b：",b)
outer()
print("a:",a)

#测试LEGB规则

#str = 'global str'
def outer ():
   # str ="outer"
    def inner():
      # str = "inner"
        print(str)
        pass
    inner()
outer()
print(type(str))

