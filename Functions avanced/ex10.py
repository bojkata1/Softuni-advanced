from collections import deque
def fill_the_box(*args):
    args = deque(args)
    volume = args.popleft() * args.popleft() * args.popleft()
    while args:
        if args[0] == 'Finish':
            args.popleft()
            break
        if volume - args[0] < 0:
            args[0] -= volume
            volume = 0
            break
        else:
            volume -= args.popleft()
    if 'Finish' in args:
        args.remove('Finish')
    if args and volume == 0:
        return f'No more free space! You have {sum(args)} more cubes.'
    else:
        return f'There is free space in the box. You could put {volume} more cubes.'
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))