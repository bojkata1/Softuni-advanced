def even_odd(*args):
    command = args[-1]
    for num in args:
        if command == 'even':
            return list(filter(lambda x: x % 2 == 0, args[:-1]))
        elif command == 'odd':
            return list(filter(lambda x: x % 2 != 0, args[:-1]))
