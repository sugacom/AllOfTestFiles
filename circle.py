import math
class Circle:
    def __init__(self, r):
        self.radius = r

    def cal_area(self):
        return self.radius ** 2 * math.pi

cir1 = Circle(5)
print(cir1.cal_area())
