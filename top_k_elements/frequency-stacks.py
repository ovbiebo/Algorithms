from heapq import *


class Element:
    def __init__(self, number, frequency, sequence_number):
        self.number = number
        self.frequency = frequency
        self.sequence_number = sequence_number

    def __lt__(self, other):
        if self.frequency != other.frequency:
            return self.frequency > other.frequency
        return self.sequence_number > other.sequence_number


class FrequencyStack:
    sequence_number = 0
    max_heap = []
    frequency_map = {}

    def push(self, num):
        self.frequency_map[num] = self.frequency_map.get(num, 0) + 1
        heappush(self.max_heap, Element(
            num, self.frequency_map[num], self.sequence_number))
        self.sequence_number += 1

    def pop(self):
        num = heappop(self.max_heap).number
        if self.frequency_map[num] > 1:
            self.frequency_map[num] -= 1
        else:
            del self.frequency_map[num]

        return num


if __name__ == '__main__':
    frequencyStack = FrequencyStack()
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(3)
    frequencyStack.push(2)
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(5)
    print(frequencyStack.pop())
    print(frequencyStack.pop())
    print(frequencyStack.pop())
