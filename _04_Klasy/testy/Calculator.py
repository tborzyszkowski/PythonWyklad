class Calculator:
    def __init__(self) -> None:
        self.state = 0
        self.isError = False

    def add(self, number):
        self.state += number

    def substr(self, number):
        self.state -= number

    def mult(self, number):
        self.state *= number

    def reset(self):
        self.isError = False
        self.state = 0

    def div(self, number):
        if number == 0:
            self.isError = True
        else:
            self.state /= number
