__author__ = 'romarin'


# Write a function char_freq() that takes a string and builds a frequency
# listing of the characters contained in it. Represent the frequency listing
# as a Python dictionary. Try it with something like
# char_freq("abbabcbdbabdbdbabababcbcbab").


def char_freq(string=''):
    dic = {}
    for item in string:
        if item in dic.keys():
            dic[item] += 1
        else:
            dic[item] = 1
    return dic


print(char_freq("abbabcbdbabdbdbabababcbcbab"))
