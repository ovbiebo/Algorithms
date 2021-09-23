def circular_array_loop_exists(nums):
    visited = set()

    def move(index):
        if index < 0:
            return -1
        prev_index = index
        index = (index + nums[index]) % len(nums)
        if index == prev_index or ((nums[index] < 0) != (nums[prev_index] < 0)):
            return -1
        return index

    for i in range(len(nums)):
        slow = fast = i
        while True:
            slow = move(slow)
            fast = move(move(fast))
            if fast < 0 or slow < 0:
                break
            if slow == fast:
                return True

    return False


if __name__ == '__main__':
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))  # True
    print(circular_array_loop_exists([2, 2, -1, 2]))  # True
    print(circular_array_loop_exists([2, 1, -1, -2]))  # False
    print(circular_array_loop_exists([-2, 1, -1, -2, -2]))  # False
    print(circular_array_loop_exists([3, 1, 2]))  # True
    print(circular_array_loop_exists([-1, 2]))  # False
    print(circular_array_loop_exists([1, -2]))  # False
