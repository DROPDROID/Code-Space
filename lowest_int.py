def sum_two_smallest_numbers(numbers):
    checked_array = []

    #Moderation, I am checking if there is any floats or negative numbers and remove 'em.
    for number in numbers:
        if  number >= 0 and isinstance(number, int):
            checked_array.append(number)
        

    def number_loop(array_of_num):
        min_num = checked_array[0]
        for number in array_of_num:
            if number < min_num:
                min_num = number
        # here I return a min number
        return min_num
    
    #here I get first min number
    num_1 = number_loop(checked_array)

    #here I remove a min number from my array, to find second one 
    checked_array.remove(num_1)
    
    #here I get another second min number
    num_2 = number_loop(checked_array)

    return num_1 + num_2
    


sum_two_smallest_numbers([19, 5, 42, 2, 77])