# You are in an infinite 2D grid where you can move in any of the 8 directions:

#  (x,y) to
#     (x+1, y),
#     (x - 1, y),
#     (x, y+1),
#     (x, y-1),
#     (x-1, y-1),
#     (x+1,y+1),
#     (x-1,y+1),
#     (x+1,y-1)
# You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

class Point:

    def __init__(self, x, y):

        self.x = x
        self.y = y

def get_dist(p1, p2):

    x_max= abs(p1.x - p2.x)
    y_max = abs(p1.y - p2.y)
    dist = max(x_max, y_max)
    return dist

def parse_list(point_list):

    i = 0
    total_dist = 0
    while (i < len(point_list) - 1):

        temp_dist = get_dist(point_list[i], point_list[i+1])
        total_dist += temp_dist
        i += 1

    return total_dist

p1 = Point(1, 2)
p2 = Point(4, 4)
p3 = Point(14, 1)
point_list = []
point_list.append(p1)
point_list.append(p2)
point_list.append(p3)

print(parse_list(point_list))
