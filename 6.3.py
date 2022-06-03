#传值可变对象
'''
a = [10,20]

print(id(a))
print(a)
print("***********")
def test(m):
    print(id(m))
    m.append(30)
    print(id(m))
test(a)
print(a)
'''
#传值不可变对象
a = 100
def f1(n):
    print("n",id(n))
    n = n+200
    print("n",id(n))
    print(n)
f1(a)
print("a",id(a))