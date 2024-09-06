def is_isogram(string):
    string = string.lower()

    unic_letters_word = ''.join(set(string))
 
    if len(string) == len(unic_letters_word):
        return True
    else:
        return False

is_isogram('aba')
