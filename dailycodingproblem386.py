
#Given a string, sort it in decreasing order based on the frequency of characters. If there are multiple possible solutions, return any of them.

import heapq

def sort_string(s):

    result = ''
    char_list = []
    char_dict = {}
    for i in s:
        if (i not in char_list):
            char_list.append(i)
            char_dict[i] = 1
        else:
            temp = char_dict[i]
            temp += 1
            char_dict[i] = temp

    freq = []
    for key in char_dict:
        freq.append(char_dict[key])
    freq.sort()

    i = len(freq) - 1

    used_char = []
    while(i >= 0):
        for key in char_dict:
            if (char_dict[key] == freq[i] and key not in used_char):
                result = result + key*freq[i]
                used_char.append(key)
        i -= 1
    print(result)

sort_string("twitter")
    