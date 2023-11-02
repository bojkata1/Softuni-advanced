def func_executor(*args):
    result = []
    for func, func_args in args:
        result.append(f'{func.__name__} - {func(*func_args)}')
    return '\n'.join(result)

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4)),
    (sum_numbers, (2, 3))
))
