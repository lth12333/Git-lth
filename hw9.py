class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def show(self):
        print(f'({self.__x},{self.__y})')

    def set(self, x, y):
        self.__x = x
        self.__y = y

    def get(self):
        return (self.__x, self.__y)


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.lt = Point(x1, y1)
        self.rb = Point(x2, y2)

    def show(self):
        x2, y2 = self.rb.get()
        x1, y1 = self.lt.get()
        print(f'좌측 상단 꼭지점이 ({x1},{y1})이고 우측 하단 꼭지점이 ({x2},{y2})인 사각형입니다.', end = '')

    def getWidth(self):
        x2, y2 = self.rb.get()
        x1, y1 = self.lt.get()
        x = x2 - x1
        return x

    def getHeight(self):
        x2, y2 = self.rb.get()
        x1, y1 = self.lt.get()
        y = y2 - y1

    def getArea(self):
        x2, y2 = self.rb.get()
        x1, y1 = self.lt.get()
        x = x2 - x1
        y = y2 - y1
        return x * y

    def getPerimeter(self):
        x2, y2 = self.rb.get()
        x1, y1 = self.lt.get()
        x = x2 - x1
        y = y2 - y1
        return (x + y)*2

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
