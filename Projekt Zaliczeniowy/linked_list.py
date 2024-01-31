class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.size += 1

    def push_back(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if index == 0:
            self.push_front(value)
            return
        if index == self.size:
            self.push_back(value)
            return
        current = self.head
        for _ in range(index):
            current = current.next
        new_node = Node(value)
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node
        self.size += 1

    def pop_front(self):
        if self.head is None:
            raise ValueError("List is empty")
        value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return value

    def pop_back(self):
        if self.tail is None:
            raise ValueError("List is empty")
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return value

    def erase(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        if index == 0:
            return self.pop_front()
        if index == self.size - 1:
            return self.pop_back()
        current = self.head
        for _ in range(index):
            current = current.next
        value = current.value
        current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        self.size -= 1
        return value

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def find(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def remove(self, value):
        count = 0
        current = self.head
        while current:
            if current.value == value:
                next_node = current.next
                self.erase(count)
                current = next_node
            else:
                current = current.next
                count += 1
        return count

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __repr__(self):
        values = [str(node) for node in self]
        return 'List([' + ', '.join(values) + '])'
