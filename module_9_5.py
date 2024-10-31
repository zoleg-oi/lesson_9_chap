# Range - это просто
class StepValueError(ValueError):
    pass


class Iterator:
    pointer = 0
    __FLAG_FIRST = 1

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        if self.step == 0:
            raise StepValueError('шаг не может быть равен 0')

    def __iter__(self):
        # выставляем начальное значение отнимая один шаг для упрощения итераций.
        self.pointer = self.start - self.step
        return self

    def __next__(self):
        self.pointer += self.step  # Итерация
        # Условие прекращающее итерации
        # Если итерации превышают конечное значение
        # Если итерации невозможны, т.е. конечное число меньше начального, или больше, в случае отрицательного шага
        if (self.step > 0 and self.pointer > self.stop) or \
                (self.step < 0 and self.pointer < self.stop) or \
                (self.step < 0 and self.start < self.stop) or \
                (self.step > 0 and self.start > self.stop):
            raise StopIteration()

        return self.pointer


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, -1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
