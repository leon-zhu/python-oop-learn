import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        return math.sqrt((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2)


class Polygon:
    def __init__(self, points=None):
        points = points if points else []
        self.vertices = []
        for point in points:
            if isinstance(point, tuple):
                point = Point(*point)
            self.vertices.append(point)

    def add_point(self, point):
        self.vertices.append(point)

    def perimeter(self):
        perimeter = 0
        # 计算多边形周长(注意: 是闭合的)
        assert len(self.vertices) > 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i + 1])
        return perimeter


class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        print("method _set_name()")
        if not name:
            raise Exception("Invalid name")
        self._name = name

    def _get_name(self):
        print("method _get_name()")
        return self._name

    # 直接操作c.name时，那么走_get_name(), _set_name()；而直接操作c._name则不影响
    name = property(_get_name, _set_name)


class Silly:

    @property
    def silly(self):
        """This is a silly property"""
        print("You are getting silly")
        return self._silly

    @silly.setter
    def silly(self, value):
        print("You are making silly {}".format(value))

    @silly.deleter
    def silly(self):
        print("Whoah, you killed silly!")
        del self._silly

    def _get_silly(self):
        print("You are getting silly")
        return self._silly

    def _set_silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value

    def _del_silly(self):
        print("Whoah, you killed silly!")
        del self._silly

    # silly = property(_get_silly, _set_silly, _del_silly, "This is a silly property")


from urllib.request import urlopen


class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print("Retrieving New page...")
            self._content = urlopen(self.url).read()
        return self._content


class AverageList(list):
    @property
    def average(self):
        return sum(self) / len(self)
