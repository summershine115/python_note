Last_code_time = '21.11.16'
Last_review_time = '21.11.17'


# 1--Number
x = 13
y = 3.14
z = 3 + 4j

# 2--String
# index可用
a = 'ABC'

# 3--List
# 可增删改查 遍历  index可用
b = [1, 2, 3]

# 4--Tuple
# 一经声明，元素无法修改 可遍历 当只有一个元素时 要加一个逗号消除歧义   inedx可用
# 元素不变指的是tuple的每个元素，指向不变，但指向的对象本身是可变的
c = ('e', 'f', ['1', '2'])
'''
print(c)
c[2][0]='3'
c[2][1]='4'
print(c)
'''

# 5--Dict
# 由键-值对构成 用{}声明 注意:key 是不可变对象
d = {'name': 'Michael', 'age': 30}
'''
用 in 方法或者 get() 方法来查看key是否存在
'gender' in d
d.get('gender')
用 pop(key) 方法删除一个键值对
'''

# 6--Set
# 一组 key 的集合,但没有value.由于 key 不可重复,在set中没有重复的元素
# 创建一个set时需要一个 list 作为输入集合,但set里的元素是无序的
# 因为要保证无重复元素，所以set中的元素都是不可变对象，list无法作为set的元素
e = set([1, 2, 3])
'''
通过 add(key) 方法添加元素，可以重复添加但无效果
e.add(4)
通过 remove(key) 方法删除元素
e.remove(1)
set可以看做数学上无需且无重复元素的集合，因此可以进行集合运算
>>s1 = set([1,2,3])
>>>s2 = set([3,4,5])
>>>s1 & s2
{3}
>>>s1 | s2
{1,2,3,4,5}
'''

# 7--不可变对象
'''
不可变对象本身的指向永远不会改变
所以，对于不可变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
例如 str 类型
>>>a = 'abc'
>>>a
'abc'
>>>a.replace('a','A')
'Abc'
>>>a
'abc'
'''

# function 函数部分

# 8--默认参数
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面
# 注意： 定义默认参数必须指向不变对象 否则再次调用时会与第一次调用结果不一致


# 这里的n=2意味着 参数n的默认值为2 但可以输入其他值来改变n的值
def func1(x, n=2):
    s = 1
    while (n > 0):
        n -= 1
        s = s * x
    return s


# 9--可变参数  (数量可变)
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
# 注意： 定义可变参数时 仅仅只多出一个 * 号
def func2(*number):
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum


# Python支持在list或tuple前面加上一个*来作为可变参数传入函数
'''
>>>nums = [1,2,3]
>>>func2(*nums)
13
'''


# 10--关键字参数
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
# 注意： 定义关键字参数时 用 ** 作为标记
def func3(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# 在调用函数时 可以只传入必选参数
'''
>>>func3('Bob',30)
name: Bob age: 30 other: {}
'''
# 也可传入任意个数的关键字参数
'''
>>>func3('Bob',30,city='WuHan')
name: Bob age: 30 other: {'city': 'WuHan'}
'''
"""  """

# 11--命名关键字参数
# 关键字函数在输入需要的参数后还可以输入任意的参数,为了对关键字参数加以限定

# 命名关键字需要一个特殊分隔符 * , * 后的参数被视为命名关键字参数
'''
例如只接收 city 和 job 作为关键字参数


'''


def func4(name, age, *, city, job):
    print(name, age, city, job)


'''
如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符 * 了
'''


def func5(name, age, *args, city, job):
    print(name, age, args, city, job)


# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
'''
>>> func4('Jack', 24, 'Beijing', 'Engineer')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: person() missing 2 required keyword-only arguments: 'city' and 'job'
'''
# 命名关键字参数可以有缺省值，从而简化调用
'''
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
'''

# 12--参数组合
# python中定义参数可以使用必选参数,默认参数,可变参数,命名关键字参数和关键字参数
# 注意: 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
