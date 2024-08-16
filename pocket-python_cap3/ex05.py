<<<<<<< HEAD
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector(self.x / other.x, self.y / other.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(30, 40)
v2 = Vector(10, 20)

result_mul = v1 * v2
result_div = v1 / v2


print(f"v1 * v2 = {result_mul}")
print(f"v1 / v2 = {result_div}")