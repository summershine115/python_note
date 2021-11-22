Last_code_time = '21.11.20'
Last_review_time = '21.11.20'

# List comprehension 如字面意思,列表推导式,从一个给出的条件推导出所有满足要求的元素项
# 是构建list的快捷方式

# 语法
'''
Lname = [表达式 for 形参 in range ]
'''

# 列表推导式的优点:
# 代码简洁,可读性高

# 缺点:
# 无法完成复杂的任务
'''
例如,想要打印一到十所有整数的平方

可以采用循坏实现:

l = []
for x in range(1,11):
    l.append(x * x)
print(l)

也可以采用列表推导式实现:

l = [x * x for x in range(1,11)]
print(l)

'''

# if ... else
'''
在表达式中可以加入if...else对结果再加以限定
例如输出1-10中的偶数

>>> list=[x for x in range(1,11) if x % 2 == 0]
>>> list
[2,4,6,8,10]
'''

# 但是 不能再最后的if加上else
'''
>>> [x for x in range(1, 11) if x % 2 == 0 else 0]
  File "<stdin>", line 1
    [x for x in range(1, 11) if x % 2 == 0 else 0]
                                               ^
SyntaxError: invalid syntax
'''

