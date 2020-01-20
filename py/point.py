class Point:
    def __init__(self, x, y, z=None):
        self.x = x
        self.y = y
        self.z = z

    def ToString(self):
        if self.z is None:
            print("x : %.2f / y : %.2f " % (self.x, self.y))
        else:
            print("x : %.2f / y : %.2f / z : %.2f " % (self.x, self.y, self.z))


P1=Point(2, 3)
P1.ToString()
P2=Point(1, -5, 6)
P2.ToString()
