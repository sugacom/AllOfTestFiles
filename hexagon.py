class Hexagon:
    def __init__(self, d):
        self.diameter = d

    def cal_perimeter(self):
        return self.diameter / 2 * 6

hex1 = Hexagon(3)
print(hex1.cal_perimeter())
