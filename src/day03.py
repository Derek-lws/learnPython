"""
	date:2020.04.15
	author:Derek_lws
"""
L = []
for x in range(10):
	L.append(x**2)
	print(L[x])

L = [x**2 for x in range(10)]#表推导(快速生成表)
for x in L:
	print(x)

def gen():
    a = 100
    yield a
    a = a*8
    yield a
    yield 1000
for x in gen():#生成器(构成一个用户自定义循环对象，yield后返回值)
	print(x)

def ben():
    for i in range(4):
        yield i**2
for x in ben():
	print(x)

G = (x**2 for x in range(7))#生成器表达式
for x in G:
	print(x)

list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")

S = 'abcdefghijk'
for i in range(0,len(S),2):#range()
    print(S[i])

for (index,char) in enumerate(S):#enumerate()
    print(index)
    print(char)

ta = [1,2,3]
tb = [9,8,7]
tc = ['a','b','c']
for (a,b,c) in zip(ta,tb,tc):#zip()
    print(a,b,c)

function = lambda m,n: m ** n
print(function(3,4))#便捷定义函数输入：输出

def test(f, a, b):
    print('test')
    print(f(a, b))
test((lambda x,y: x**2 + y), 6, 9)#函数作为参数传递

re = map((lambda x,y: x+y),[1,2,3],[6,7,9])
#map()的功能是将函数对象依次作用于表的每一个元素
#返回值是一个循环对象
for x in re:
	print(x)

def func(a):
    if a > 100:
        return True
    else:
        return False

rs = filter(func,[10,56,101,500])
#filter()过滤True返回值存入循环对象

for x in rs:
	print(x)

re = iter(range(5))

try:
    for i in range(100):
        print (re.__next__())
except StopIteration:
    print('here is end ',i)

print ('HaHaHaHa')

re = iter(range(5))
try:
    for i in range(10):
        # print(re.__next__())
        print(next(re))
except StopIteration:
    print("-----iter is end-----")
finally:
    print("haha")
#python3中next()写成__next__(),next(re)，finally在我这儿理解就是如果try部分没有异常，则继续执行finally部分。
try:
    a = int(input("please input number:"))
    if a > 50:
        print("True")
    else:
        print("False")
except ValueError:
    print("valueerror")
else:
    print(a)
#reise StopIteration() 自己抛出异常
def f(x):
    x = 100
    print (x)

a = 1
f(a)
print (a)

def f(x):
    x[0] = 100
    print(x)

a = [1,2,3]
f(a)
print(a)#引用和对象的分离，对象是内存中储存数据的实体，引用指向对象。

#可变对象，不可变对象

#函数值传递

