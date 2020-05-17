# 0
class Point3D:
    x = 0
    y = 0
    z = 0


p1 = Point3D()
p2 = Point3D()
p3 = Point3D()
print("X:", p1.x, "Y:", p1.y, "Z:", p1.z)
print("X:", p2.x, "Y:", p2.y, "Z:", p2.z)
print("X:", p3.x, "Y:", p3.y, "Z:", p3.z)

# 1
Point3D.x = 10
print("X:", p1.x, "Y:", p1.y, "Z:", p1.z)
print("X:", p2.x, "Y:", p2.y, "Z:", p2.z)
print("X:", p3.x, "Y:", p3.y, "Z:", p3.z)

# 2
delattr(Point3D, "z")
print("X:", p1.x, "Y:", p1.y, "Z:", p1.z)
print("X:", p2.x, "Y:", p2.y, "Z:", p2.z)
print("X:", p3.x, "Y:", p3.y, "Z:", p3.z)

# 3
p2.y = 20
print("X:", p1.x, "Y:", p1.y, "Z:", p1.z)
print("X:", p2.x, "Y:", p2.y, "Z:", p2.z)
print("X:", p3.x, "Y:", p3.y, "Z:", p3.z)
