class AdvancedCalculator:
    def __init__(self):
        self.memory = 0

    def add(self, a, b):
        self.memory = a + b
        return self.memory

    def subtract(self, a, b):
        self.memory = a - b
        return self.memory

    def multiply(self, a, b):
        self.memory = a * b
        return self.memory

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Kan niet delen door 0.")
        self.memory = a / b
        return self.memory

    def power(self, a, b):
        self.memory = a ** b
        return self.memory

    def recall_memory(self):
        return self.memory

    def clear_memory(self):
        self.memory = 0
