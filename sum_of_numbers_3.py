def get_sum(a,b):
    if a == b:
        return a
    elif a < b:
        return sum(list(range(a, b+1)))
    elif a > b:
        return sum(list(range(b, a+1)))


get_sum(-2, -1)