def maskify(cc):
    #amount of digits without last four
    len_of_str = len(cc) - 4
    #cuts four visible digits
    visible_digits = cc[len_of_str:]
    if len(cc) > 4:
        return (str )('#' * len_of_str + visible_digits)
    else:
        return (str)(cc)
    
maskify('SF$SDfgsd2eA')