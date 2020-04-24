def print_each(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        else:
            print(item)


_list = ['apple', 'peach', 'banana', 'grapes']

print_each(_list)