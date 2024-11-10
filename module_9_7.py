# Декораторы
def is_prime(func):
    def wrapper(*args):
        s = func(*args)
        w = 0
        for i in range(2, s // 2 + 1):
            if s % i == 0:
                w += 1
        if w <= 0:
            return f'{s}\nПростое'
        else:
            return f'{s}\nСоставное'

    return wrapper


@is_prime
def sum_three(*args):
    summa = sum(args)
    return summa


result = sum_three(2, 3, 6)
print(result)
