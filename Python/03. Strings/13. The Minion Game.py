"""My awful soluton"""
def minion_game(string):
    count_vowels = 0
    count_consonants = 0
    vowels = 'AEIOU'
    result = set()
    for i in range(len(string)):
        for x in range(i+1, len(string)+1):
            result.add(string[i:x])
    for i in range(len(string)):
        for j in result:
            if string[i:].startswith(j) and j[0] in vowels:
                count_vowels += 1
            elif string[i:].startswith(j) and j[0] not in vowels:
                count_consonants +=1
    if count_vowels == count_consonants:
        print('Draw')
    elif count_vowels > count_consonants:
        print('Kevin', count_vowels)
    else:
        print('Stuart', count_consonants)

if __name__ == '__main__':
    s = input()
    minion_game(s)

"""My good solution"""
def minion_game(string):

    count_vowels = 0
    count_consonants = 0
    vowels = 'AEIOU'
    len_of_str = len(string)
    for i in range(len_of_str):
        if string[i] in vowels:
            count_vowels += len_of_str - i
        else:
            count_consonants += len_of_str - i
    if count_vowels == count_consonants:
        print('Draw')
    elif count_vowels > count_consonants:
        print('Kevin', count_vowels)
    else:
        print('Stuart', count_consonants)

if __name__ == '__main__':
    s = input()
    minion_game(s)