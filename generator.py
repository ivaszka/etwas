# Создайте итерируемый объект, возвращающий генератор тридцати пяти чисел трибоначчи и выведите эти числа.

class ThreeBonacciGenerator:
    def __init__(self, length):
        self.length = length

    def __iter__(self):
        first = 0
        yield first
        second = 0
        yield second
        third = 1
        yield third
        for i in range(self.length-3):
            temp2 = second
            temp3 = third
            third = first + second + third
            second = temp3
            first = temp2
            yield third


size = 35
numbers = ThreeBonacciGenerator(size)
for number in numbers:
    print(number)
