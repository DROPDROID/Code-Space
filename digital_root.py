def digital_root(n):
    
    def breaker(num):
        result = 0
        for i in str(num):
            result += int(i)
        return result
            

    while len(str(n)) > 1:
        n = breaker(n)

    return n


digital_root(16)