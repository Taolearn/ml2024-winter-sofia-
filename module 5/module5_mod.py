# module5_mod.py

class NumberManager:
    def __init__(self):
        self.numbers = []

    def read_n_numbers(self, n):
        for i in range(n):
            num = int(input(f"Enter number {i + 1}: "))
            self.numbers.append(num)

    def find_index_of_x(self, x):
        for i, num in enumerate(self.numbers, 1):
            if num == x:
                return i
        return -1
