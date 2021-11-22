Last_code_time = '21.11.18'
Last_review_time = '21.11.18'

# 迭代&迭代器
'''
迭代: 是一种访问集合元素的方式 (所有的序列, 字典, 集合)
迭代器: 是一个可以记住遍历位置的对象,
    从集合的第一个元素开始访问,直到所有的对象被访问完毕结束
    迭代器只能往前不会后退
'''

# 迭代器有两个基本方法: iter(), next()
# iter() : 用于创建迭代器对象
# next() : 用于访问迭代器的下一个元素
'''
>>> list=[1,2,3,4]
>>> it = iter(list)    # 创建迭代器对象
>>> print (next(it))   # 输出迭代器的下一个元素
1
>>> print (next(it))
2
'''

# 迭代器对象可用 for 循环来遍历
'''
>>> list=[1,2,3,4]
>>> it = iter(list)    # 创建迭代器对象
>>> for x in it:
...     print (x, end=" ")
1 2 3 4
'''

# 创建一个迭代器
'''
把类作为一个迭代器使用 需要在类中实现两个方法 iter() next()
'''

# class numbers:
#     def __iter__(self):
#         self.a = 0
#         return self

#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x

#     pass

# num = numbers()
# numiter = iter(num)

# for x in numiter:
#     if x <= 20:
#         print(x)

# StopIteration
'''
StopIteration 异常用于宝石迭代的完成,防止出现无限循环的情况,
在 next() 方法中我们可以设置在完成指定循环次数后触发topIteration异常来结束迭代
'''


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
