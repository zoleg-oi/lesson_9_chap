# Вызов разом

def apply_all_func(int_list, *functions):
    results = {}
    for fun in functions:
        try:
            results[fun.__name__] = fun(int_list)
        except TypeError:
            results[fun.__name__] = "Операции возможны только с числами"

    return results


print(apply_all_func([6, "f", 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
