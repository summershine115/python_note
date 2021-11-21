Last_code_time = '21.11.17'
Last_review_time = '21.11.17'


'''
引入:

矛盾:  传统的list创建方式存在着 空间使用不合理 的弊端

通过列表生成式我们能直接创建一个列表,但受到内存限制,列表的容量肯定是有限的
而且如果生成一个包含1,000,000个元素的列表,不仅展荣非常大的储存空间,
如果我们仅仅需要访问前面几个元素那么后面绝大多数的空间都白白浪费了
'''
'''
解决方案:  生成器

如果列表元素可以通过某种算法推算出来,那么我们是否可以在循环的过程中不断推理出后续的元素呢?
这样就不必创建完整的list,从而节省大量的储存空间,在python中,这种一边循环一边计算的机制，
称为生成器：Generator
'''

# 创建一个generator有很多种方式

# 1--只要把一个列表生成式的[]改成(),就创建了一个generator

L = [x * x for x in range(10)]

g = (x * x for x in range(10))

# generator所生成的值无法全部打印出来
# 如果要一个一个打印出来,需要使用 next() 函数来获得generator的下一个返回值
'''
>>>next(g)
0
>>>next(g)
1
...
'''
# 但这种方式应对许多输出时十分麻烦,这时需要使用 for 循环来出输出,因为generator也是一个可迭代对象
'''
>>> g = (x * x for x in range(5))
>>> for n in g:
...     print(n)
...
0
1
4
9
16
'''

# 如果推算的算法比较复杂,用 for 循环无法实现时,可以用函数来实现
# 比如输出斐波那契数列的前n项


def fibo(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'


# fibo(10)

# 这个 fibo() 函数已经与generator仅一步之遥,要把 fibo() 变成generator函数,只需要把print(b)改为 yield b 就可以了
# 2--这就是定义generator的另一种方式 generator函数
'''
如果函数定义中包含 yield 关键字,那么这个函数就不再是一个普通函数
而是一个generator函数,调用generator函数将返回一个generator
注意: 多次调用会创建多个相互独立的generator
'''


def fibo1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


'''
在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，
返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。

但是我们在循环中不断调用 yield 就不会中断,要给循环设置一个退出条件,否则会产生一个无限数列出来

同样的,把函数改成generator函数后,通常会使用for循环来迭代

>>> for n in fib(6):
...     print(n)
...
1
1
2
3
5
8
'''

# 但是用 for 循环调用generator时,发现拿不到generator的return值,如果想要拿到返回值,
# 必须捕获 stopIteration 错误,返回值包含在 stopIteration的value中
'''
>>> g = fib(6)
>>> while True:
...     try:
...         x = next(g)
...         print('g:', x)
...     except StopIteration as e:
...         print('Generator return value:', e.value)
...         break
...
g: 1
g: 1
g: 2
g: 3
g: 5
g: 8
Generator return value: done
'''

# 练习 杨辉三角

# 把每一行看做一个list，试写一个generator，不断输出下一行的list：

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# ...

# 代码


def triangles(max):
    L = [1]
    a = 1
    while a <= max:
        yield (L)
        L = [
            1 if i == 0 or i == len(L) else L[i - 1] + L[i]
            for i in range(len(L) + 1)
        ]
        a += 1


# for n in triangles(10):
#     print(n)
