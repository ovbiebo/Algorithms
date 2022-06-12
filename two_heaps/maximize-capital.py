from heapq import *


def find_maximum_capital(capital, profits, number_of_projects, initial_capital):
    min_capitals_heap = []
    max_profit_heap = []
    balance = initial_capital

    for i, amount in enumerate(capital):
        heappush(min_capitals_heap, (amount, i))

    for i in range(number_of_projects):
        while min_capitals_heap and balance >= min_capitals_heap[0][0]:
            required_capital, profit_index = heappop(min_capitals_heap)
            heappush(max_profit_heap, -profits[profit_index])

        if not max_profit_heap:
            break

        balance += -heappop(max_profit_heap)

    return balance


if __name__ == '__main__':
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))
