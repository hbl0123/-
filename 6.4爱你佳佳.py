print("aini jiajia")
f = lambda a,b,c,d:a*b*c*d

def test(a,b,c,d):
    return a*b*c*d
print(f(2,3,4,5))
g = [lambda a:a*2,lambda b:b*3,lambda c:c*5]

print(g[0](6))

h = [test,test]
print(h[0](3,4,5,6))