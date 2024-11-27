class Calculator:
    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments should be numeric")
        return a + b

    def sub(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments should be numeric")
        return a - b

    def multi(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments should be numeric")
        return a * b

    def div(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments should be numeric")
        if b == 0:
            raise ZeroDivisionError("Cannot divide by Zero")
        return a / b
