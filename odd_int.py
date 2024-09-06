def find_it(seq):
    for a in seq:
        if seq.count(a) % 2 == 1:
            return a

find_it([1,2,2,3,3,3,4,3,3,3,2,2,1])