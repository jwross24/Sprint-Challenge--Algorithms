'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if len(word) == 0:
        return 0

    # Returns beginning index if "th" is found within word, else returns -1
    th_index = word.find("th")
    if th_index == -1:
        return 0
    else:
        return 1 + count_th(word[th_index + 2:])
