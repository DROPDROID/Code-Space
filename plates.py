def main():

    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Checks if all functions insight return True
def is_valid(s):

# Checks if word is minimum 2 character long and first two characters are letters
    def amount_of_alpha_letters(word):
        if len(word) >= 2 and word[0].isalpha() and word[1].isalpha():
            return True
        else:
            return False

# Checks if length of word is 6 characters maximum
    def max_amount_of_letters(word):
        if len(word) <= 6:
            return True
        else:
            return False

# Checks there are no numbers in the middle of the function, and it doesn't start with 0
    def no_num_middle(word):

        result = None
        
        for i in range(len(word)):
            if word[i] == '0':
                return False
            if word[i].isdigit():
                result = i
                break

        if result == None :
            return True

        elif word[result:].isdigit():
            return True


# Checks if there are no spaces, commas or full stops
    def no_punctuation(word):
        for i in word:
            if i == ' ' or i == ',' or i == '.':
                return False

        return True

# Returns True if all conditions above return True
    if amount_of_alpha_letters(s) == True and max_amount_of_letters(s) == True and no_num_middle(s) == True and no_punctuation(s) == True:
        return True
    else:
        return False

main()
