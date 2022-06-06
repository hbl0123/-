print("aini jiajia")
#测试递归的基本原理
def test(n):
    print("test",n)
    if n==0:
        print("over")
    else:
        test(n-1)

    print("test***",n)

def test01():
    print("test01")
test(4)
#使用递归函数计算阶乘（factorial）
def factorial(n):
    if n == 1:
        return 1
    return  n*factorial(n-1)
for i in range(1,6):
    print(i,'! =',factorial(i))
#分形几何
import turtle as t
def koch(size, n):
    if n == 0:
        t.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
              t.left(angle)
              koch(size / 3, n - 1)
if __name__ == '__main__':
    t.setup(1000, 1000)
    t.pen(speed=0, pendown=False, pencolor='blue')
    a, n = 400, 4
    t.goto(-a / 2, a / 2 / pow(3, 0.5))
    t.pd()
for i in range(3):
    koch(a, n)
    t.right(120)
    t.ht()
