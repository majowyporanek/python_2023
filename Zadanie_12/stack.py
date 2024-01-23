class Stack:
    def __init__(self, max_size=10):  # Dodano argument max_size z domyślną wartością
        self.items = []
        self.max_size = max_size

    def __str__(self):  # podglądamy stos
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):  # sprawdza, czy stos jest pełny
        return len(self.items) >= self.max_size

    def push(self, item):
        if self.is_full():
            raise OverflowError("Stos jest przepełniony")  # zgłasza błąd, gdy stos jest pełny
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stos jest pusty")  # zgłasza błąd, gdy stos jest pusty
        return self.items.pop()
