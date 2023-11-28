def filter_list(l):
    new_list = []
    for item in l:
        print(type(item))
        if isinstance(item, int):
            new_list.append(item)
    'return a new list with the strings filtered out'
    print(new_list)
    return new_list


filter_list([1, 2, 3, "hello", 'world'])
