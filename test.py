def triangles(max):
    L = [1]
    a = 1
    while a <= max:
        yield(L)
        L = [1 if i == 0 or i == len(L) else L[i - 1] + L[i] for i in range(len(L) + 1)]
        a += 1


for n in triangles(10):
    print(n)
