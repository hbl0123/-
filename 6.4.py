print("aini jiajia")
#传递不可变对象时，如果发生拷贝，是浅拷贝
a = (10,20,[5,6])
print("a:",id(a))

def test(m):
    print("m:",id(m))
    m[2][0] = 888
    print(m)
    print("m:",id(a))

test(a)
print(a)
