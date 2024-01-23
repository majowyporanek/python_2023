import random


class RandomQueue:

    def __init__(self, size=10):
        self.items = []
        self.max_size = size

    def insert(self, item):
        if self.is_full():
            raise OverflowError("Kolejka jest pełna")
        self.items.append(item)

    def remove(self):
        if self.is_empty():
            raise IndexError("Kolejka jest pusta")
        index = random.randint(0, len(self.items) - 1)
        self.items[index], self.items[-1] = self.items[-1], self.items[index]
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) >= self.max_size

    def clear(self):
        self.items = []
