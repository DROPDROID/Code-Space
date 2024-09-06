def get_middle(s):
    if len(s) % 2 == 0:
        index_of_characters = int((len(s)-1) / 2)
        return s[index_of_characters] + s[index_of_characters + 1]
    else:
        index_of_character = int(len(s) / 2)
        return s[index_of_character]


get_middle('test')
