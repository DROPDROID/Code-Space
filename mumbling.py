def accum(st):
    num = 0
    multiplied_letters  = ''
    result = ''
   
    for i in st:
      num += 1
      multiplied_letters = (i * num + '-')
      result += multiplied_letters.capitalize()
    
    return result.strip('-')
      

accum('abc')