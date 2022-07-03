filter() 相当于过滤器的作用
s=[1,2,3,5,6,8,9,10,25,12,30]
#### 筛选出3的倍数
#### 第一个参数为一个返回True或者False的函数，第二个参数为可迭代对象
#### 该函数把可迭代对象依次传入第一个函数，如果为True，则筛选
d=filter(lambda x:True if x % 3 == 0 else False,s)
print(list(d))
map()函数，
#### 第一个参数为函数，依次将后面的参数传给第一个函数，并执行函数
#### 如果有多个参数则，依次将后面的对应传给参数
s=map(lambda x,y:x+y,range(10),range(10))
print(list(s))
ss=map(lambda x:x*x,range(10))
print(list(ss))
reduce()函数
from functools import reduce
#### 开始的时候将可迭代对象的第一个数和第二个数当成x和y
#### 然后将第一次函数的执行结果当成x，然后再传入一个数当成y
#### 再执行函数
s=reduce(lambda x,y:x+y,range(101))
print(s) # 相当于0+1+2+……+99+100