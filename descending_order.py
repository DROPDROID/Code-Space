def descending_order(num):
    result = ''
    sorted_list = sorted(str(num))
    reversed_list = sorted_list[::-1]

    for i in reversed_list:
        result += i

    return int(result)
        

descending_order(321)