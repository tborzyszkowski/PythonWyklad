class Calculator:
    def __init__(self) -> None:
        self.state = 0

    def add(self, number):
        self.state += number

    def mult(self, number):
        self.state *= number