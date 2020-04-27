import numpy

v1 = numpy.ones([3, 4], dtype=numpy.uint8)
v2 = numpy.ones_like(v1)
v3 = numpy.ones_like(
    [
        [1, 2, 3],
        [3, 2, 1]
    ]
)
print(v1)
print(v2)
print(v3)

v4 = numpy.zeros([3, 4], dtype=numpy.uint8)
v5 = numpy.zeros_like(v4)
v6 = numpy.zeros_like(
    [
        [1, 2, 3],
        [3, 2, 1]
    ]
)
print(v4)
print(v5)
print(v6)

v7 = numpy.empty([3, 4], dtype=numpy.uint8)
v8 = numpy.empty_like(v7)
print(v7)
print(v8)

v9 = numpy.eye(4)
print(v9)

v10 = numpy.eye(3)
print(v10)

v11 = numpy.eye(4, k=-1)
print(v11)
