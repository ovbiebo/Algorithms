def count_trees(n):
    count = 0

    if n <= 1:
        return 1

    for i in range(1, n + 1):
        left = count_trees(i - 1)
        right = count_trees(n - i)
        count += left * right

    return count


if __name__ == '__main__':
    print(f"Total trees: {count_trees(2)}")
    print(f"Total trees: {count_trees(3)}")
