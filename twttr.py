def omitting_vowels():
    
    sentence = input('Input: ')
    list_of_words = []

    list_of_words = [i for i in sentence if i not in 'aeiouAEIOU' ]
    result = ''.join(list_of_words)

    print(result)

omitting_vowels()
