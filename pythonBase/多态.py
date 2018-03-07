class Triangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def getArea(self):
        area = self.width * self.height / 2
        return area


class Square:
    def __init__(self,size):
        self.size = size

    def getArea(self):
        area = self.size * self.size
        return area


t = Triangle(3,1)
print(t.getArea())

s = Square(5)
print(s.getArea())