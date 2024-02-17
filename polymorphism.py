class Shape:
    def draw(self):
        print("Drawing shape")


class Square:
    def draw(self):
        print("Drawing square")

class Rectangle:
    def draw(self):
        print("Drawing rectangle")

s = Shape()
s.draw()

sq = Square()
sq.draw()

r = Rectangle()
r.draw()