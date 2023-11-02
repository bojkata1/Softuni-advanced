def separate_nums(*args):
    negative_sum = 0
    positive_sum = 0
    for num in args:
        if num < 0:
            negative_sum += num
        elif num > 0:
            positive_sum += num
    #negative_sum = sum(list(filter(lambda x: x < 0, args)))
    #positive_sum = sum(list(filter(lambda x: x > 0, args)))

    print(negative_sum)
    print(positive_sum)
    if abs(negative_sum) > positive_sum:
        print('The negatives are stronger than the positives')
    elif abs(negative_sum) < positive_sum:
        print('The positives are stronger than the negatives')
numbers = [int(x) for x in input().split()]
separate_nums(*numbers)
