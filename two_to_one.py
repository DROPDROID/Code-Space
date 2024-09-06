a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

def longest(a1, a2 = None):

    #gives me a list with sorted letters
    def make_array(var):
        return sorted(var)
    
    if a1 == a2:
        #removes duplicates
        sorted_array = list(dict.fromkeys(make_array(a1))) 
        result = ''.join(sorted_array)
    else:
        c = a1 + a2
        #removes duplicates
        sorted_array = list(dict.fromkeys(make_array(c))) 
        result = ''.join(sorted_array)
    
    return result
    
longest(a,b)