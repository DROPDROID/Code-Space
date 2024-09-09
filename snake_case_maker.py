def snake_case_maker():
    snake_case = input('camelCase: ')
    word_list = []

    for i in snake_case:
        if i.isupper():
            word_list.append('_')
            word_list.append(i.lower())
        else:
            word_list.append(i)

    snake_case = ''.join(word_list)
    print(snake_case)

snake_case_maker()


##############################################################################################################################################################################################################################################################################################################################


def snake_case_maker():
    snake_case = input('camelCase: ')


    for i in range(len(snake_case)):
        if snake_case[i] == snake_case[i].capitalize():
            snake_case = snake_case.replace(snake_case[i], f'_{snake_case[i].lower()}')

    print(snake_case)


snake_case_maker()
