def even_parameters(function):
    def wrapper(*args):
        for num in args:
            if type(num) != int or num % 2 != 0:
                return "Please use only even numbers!"
        else:
            result = function(*args)
            return result
    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
