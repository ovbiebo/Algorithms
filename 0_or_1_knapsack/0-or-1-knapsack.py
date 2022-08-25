def solve_knapsack(profits, weights, capacity):
    return solve_knapsack_tabulation(profits, weights, capacity)


def solve_knapsack_recursive(profits, weights, capacity, index=0, total_profit=0):
    if capacity < 0:
        return 0
    if index == len(weights):
        return total_profit
    return max(
        solve_knapsack_recursive(profits, weights, capacity, index + 1, total_profit),
        solve_knapsack_recursive(profits, weights, capacity - weights[index], index + 1, total_profit + profits[index])
    )


def solve_knapsack_recursive_memoized(profits, weights, capacity, index=0, total_profit=0, history=None):
    if history is None:
        history = [[-1 for c in range(capacity + 1)] for w in weights]
    if capacity < 0:
        return 0
    if index == len(weights):
        return total_profit
    if history[index][capacity] > -1:
        return history[index][capacity]
    max_profit = max(
        solve_knapsack_recursive_memoized(profits, weights, capacity, index + 1, total_profit, history),
        solve_knapsack_recursive_memoized(
            profits, weights, capacity - weights[index], index + 1, total_profit + profits[index], history
        )
    )
    history[index][capacity] = max_profit
    return max_profit


def solve_knapsack_tabulation(profits, weights, capacity):
    history = [[0 for c in range(capacity + 1)] for w in weights]

    for i, max_profits in enumerate(history):
        for capacity in range(len(max_profits)):
            if i == 0:
                if capacity >= weights[i]:
                    max_profits[capacity] = profits[i]
            else:
                prev_max_profits = history[i - 1]
                if capacity >= weights[i]:
                    remaining_capacity = capacity - weights[i]
                    max_profits[capacity] = profits[i] + prev_max_profits[remaining_capacity]
                else:
                    max_profits[capacity] = prev_max_profits[capacity]

    return history[-1][-1]


if __name__ == '__main__':
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
