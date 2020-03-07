'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    empty_string = ''
    
    if word == empty_string:
        return 0   
        lowercase = word.casefold()
        num = lowercase.count('th')
        
        if num != 0:
            count = num
            return num
    return count - count_th(word)
        
