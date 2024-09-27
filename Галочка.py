from functools import total_ordering


@total_ordering
class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.name}({self.x}, {self.y})'

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return self.x, self.y

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def __repr__(self):
        return f"Point('{self.name}', {self.x}, {self.y})"

    def __gt__(self, other):
        return (self.name > other.name or (self.name > other.name and self.x > other.x) or
                (self.name > other.name and self.x > other.x and self.y > other.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class CheckMark:
    def __init__(self, *points):
        self.points = list(points)

    def __str__(self):
        return ''.join(i.name for i in self.points)

    def __bool__(self):
        return False if len(set(i.x for i in self.points)) == 1 or len(set(i.y for i in self.points)) == 1 or len(
            set(i.get_coords() for i in self.points)) != len(self.points) or (
            float(str(((self.points[2].y - self.points[1].y) ** 2 +
                       (self.points[2].x - self.points[1].x) ** 2) ** 0.5 /
                      (self.points[2].x - self.points[1].x))[
                                :str(float(((self.points[2].y - self.points[1].y) ** 2 +
                                           (self.points[2].x - self.points[1].x) ** 2) ** 0.5 /
                                           (self.points[2].y - self.points[1].y))).index('.') + 2]) ==
            float(str(((self.points[1].y - self.points[0].y) ** 2 +
                       (self.points[1].x - self.points[0].x) ** 2) ** 0.5 /
                      (self.points[1].x - self.points[0].x))[
                                :str(float(((self.points[1].y - self.points[0].y) ** 2 +
                                           (self.points[1].x - self.points[0].x) ** 2) ** 0.5 /
                                           (self.points[1].y - self.points[0].y))).index('.') + 2])
            if self.points[2].x - self.points[1].x and self.points[1].x - self.points[0].x and
            self.points[2].y - self.points[1].y and self.points[1].y - self.points[0].y else False) else True

    def __eq__(self, other):
        return {self.points[0].get_coords(), self.points[2].get_coords()} == {other.points[0].get_coords(),
                                                                              other.points[2].get_coords()} \
            and self.points[1].get_coords() == other.points[1].get_coords()
