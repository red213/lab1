class Check(object):
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def check(self):
        try:
            int(self.num1) and int(self.num2)
            return True
        except ValueError:
            return False


class Calculator(object):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def devide(self, num1, num2):
        return num1 / num2

    def power(self, num1, num2):
        return num1 ** num2

    def remainder(self, num1, num2):
        return num1 // num2

    def inc(self, num1):
        return num1 + 1

    def dec(self, num1):
        return num1-1

    def abs(self, num1):
        return abs(num1)

    def module(self, num1, num2):
        return num1 % num2

    def pow2(self, num1, num2):
        return num2 ** num1

class Operations(Calculator):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def choice(self):
        operation = str(input("Print operation: "))
        switcher = {'+': self.add(self.num1, self.num2),
                    '-': self.subtract(self.num1, self.num2),
                    '*': self.multiply(self.num1, self.num2),
                    '/': self.devide(self.num1, self.num2),
                    '**': self.power(self.num1, self.num2),
                    '//': self.remainder(self.num1, self.num2),
                    'inc': self.inc(self.num1),
                    'dec': self.dec(self.num1),
                    'abs': self.abs(self.num1),
                    'mod': self.module(self.num1, self.num2),
                    'pow2': self.pow2(self.num1, self.num2)}
        result = switcher.get(operation)
        return result




