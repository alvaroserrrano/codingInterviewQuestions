#  You are given given a list of rectangles represented by min and max x - and
#  y-coordinates. Compute whether or not a pair of rectangles overlap each other.
#  If one rectangle completely covers another, it is considered overlapping.
#  {
#  "top_left": (1, 4),
#  "dimensions": (3, 3) # width, height
#  },
#  {
#  "top_left": (-1, 3),
#  "dimensions": (2, 1)
#  },
#  {
#  "top_left": (0, 5),
#  "dimensions": (4, 3)
#  }

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "x={}, y={}".format(self.x, self.y)


class Rectangle:
    def __init__(self, json):
        self.top_left = Point(json["top_left"][0], json["top_left"][1])
        width, height = json['dimensions']
        self.bottom_right = Point(
            self.top_left.x + width, self.top_left.y + height)

    def __repr__(self):
        return "(top-left corner={}, bottom right={})".format
        (self.top_left, self.bottom_right)

    def contains_inner(self, other):
        return self.top_left.x <= other.top_left.x and \
            self.top_left.y >= other.top_left.y and \
            self.bottom_right.x >= other.bottom_right.x and \
            self.bottom_right.y <= other.bottom_right.y


def contains_overlapping(rectangles):
    n = len(rectangles)
    for i in range(n-1):
        for j in range(i+1, n):
            if rectangles[i].contains_inner(rectangles[j]) or \
                    rectangles[j].contains_inner(rectangles[i]):
                        return True
    return False


# Tests

# example provided in the question is incorrect
r1 = Rectangle({"top_left": (1, 4), "dimensions": (3, 3)})
r2 = Rectangle({"top_left": (-1, 3), "dimensions": (2, 1)})
r3 = Rectangle({"top_left": (0, 5), "dimensions": (4, 4)})
assert contains_overlapping([r1, r2, r3])

r1 = Rectangle({"top_left": (1, 4), "dimensions": (3, 3)})
r2 = Rectangle({"top_left": (-1, 3), "dimensions": (2, 1)})
r3 = Rectangle({"top_left": (0, 5), "dimensions": (4, 3)})
assert not contains_overlapping([r1, r2, r3])
