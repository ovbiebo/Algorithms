from heapq import *


def minimum_cost_to_connect_ropes(ropeLengths):
    min_cost = 0
    heapify(ropeLengths)

    while len(ropeLengths) > 1:
        cost = heappop(ropeLengths) + heappop(ropeLengths)
        min_cost += cost
        heappush(ropeLengths, cost)

    return min_cost


if __name__ == '__main__':
    print(f"Minimum cost to connect ropes: {minimum_cost_to_connect_ropes([1, 3, 11, 5])}")  # 33
    print(f"Minimum cost to connect ropes: {minimum_cost_to_connect_ropes([3, 4, 5, 6])}")  # 36
    print(f"Minimum cost to connect ropes: {minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])}")  # 42
