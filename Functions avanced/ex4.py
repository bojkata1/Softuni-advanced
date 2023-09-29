def even_odd_filter(**kwargs):
    if 'odd' in kwargs.keys():
        kwargs['odd'] = [x for x in kwargs['odd'] if x % 2 != 0]
    if 'even' in kwargs.keys():
        kwargs['even'] = list(filter(lambda x: x % 2 == 0, kwargs['even']))
    return dict(sorted(kwargs.items(), key=lambda kvp: -len(kvp[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
