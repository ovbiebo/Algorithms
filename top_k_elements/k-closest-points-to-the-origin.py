from heapq import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print(f"[{str(self.x)}, {str(self.y)}]")

    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    def distance_from_origin(self):
        return (self.x**2) + (self.y**2)


def find_closest_points(points, k):
    result = []

    for i in range(len(points)):
        dist = points[i].distance_from_origin()
        if i < k or dist < result[0].distance_from_origin():
            heappush(result, points[i])
        if len(result) > k:
            heappop(result)

    return result


if __name__ == '__main__':
    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print(f"Here are the k points closest to the origin: ")  # 5
    for point in result:
        point.print_point()
