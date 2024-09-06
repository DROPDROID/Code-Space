def persistence(n):
    times = 0
    if len(str(n)) != 1:
        while len(str(n)) != 1:
            result = map(int, str(n))
            n = 1
            for item in result:
                n *= item
            times += 1
        return times
    else:
        return 0

persistence(39)