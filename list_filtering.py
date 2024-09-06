def filter_list(l):
    sorted_list = []
    for i in l:
        if type(i) == int:
            sorted_list.append(i)

    return sorted_list


filter_list([1,2,'a','b'])
