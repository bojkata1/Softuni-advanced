def even_odd(*args):
    result = []
    command = args[-1]
    for num in args:
        if num == command:
            break
        if command == 'even':
            if num % 2 == 0:
                result.append(num)
        elif command == 'odd':
            if num % 2 != 0:
                result.append(num)
    return result
