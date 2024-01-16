from node import Node

"""ZADANIE 11.1"""


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0  # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        # return self.length == 0
        return self.head is None

    def count(self):  # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:  # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):  # klasy O(1)
        if self.head:  # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):  # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:  # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None  # czyszczenie łącza
        self.length -= 1
        return node  # zwracamy usuwany node

    # ZADANIE 11.1 (SINGLELIST)
    def remove_tail(self):  # klasy O(n)
        # Zwraca cały węzeł, skraca listę.
        # Dla pustej listy rzuca wyjątek ValueError.
        if self.is_empty():
            raise ValueError("pusta lista")
        if self.head == self.tail:  # self.length = 1
            deleted_node = self.head
            self.head = self.tail = None
        else:
            node = self.head
            while node.next != self.tail:
                node = node.next
            self.tail = node
            deleted_node = node.next
            node.next = None
            self.length -= 1
        return deleted_node

    def join(self, other):
        if self.head is None:
            self.head, self.tail = other.head, other.tail
        elif other.head is not None:
            self.tail.next = other.head
            self.tail = other.tail

        other.head = None
        other.tail = None

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0
