import numpy

a = numpy.array([
    [1, 2, 3, 4, 5, 6, 7, 8],
    [9, 10, 11, 12, 13, 14, 15, 16]
])
new_a = a.copy()
new_a[0, 0] = 200
print(a, new_a)

b = a
b[0, 0] = 300
print(a)
print(b)

b.shape = (2, 2, 4)
print("A", a)
print("B", b)

a.resize((2, 8))
c = a.view()
c.shape = (2, 2, 4)
print('A', a)
print('C', c)
print(c.base)
