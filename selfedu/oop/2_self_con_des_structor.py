# 1
class Point3D:
    coords = [1, 2, 3]

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def change(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_attrs(self):
        return self.x, self.y, self.z


p1 = Point3D(2, 3, 6)
p1.get_attrs()
print(p1.get_attrs())
p1.change(3, 5, 7)
print(p1.get_attrs())


# 2
class Point:

    def __init__(self, x=0, y=10):
        self.x = x
        self.y = y
