def friend(x):

    for i in list(x):
        if len(i) != 4:
            x.remove(i)
    return x


friend({"Ryan", "Kieran", "Jason", "Yous"})
