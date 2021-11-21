Last_code_time = '21.11.20'
Last_review_time = '21.11.20'

# List comprehension 如字面意思,列表推导式,从一个给出的条件推导出所有满足要求的元素项

# 语法
'''
Lname = [表达式 for 形参 in range]
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
