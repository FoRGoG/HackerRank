def print_rangoli(size):
    list = []
    alphabet = [chr(i) for i in range(97, 123)]
    for i in range(size):
        line = '-'.join(alphabet[i:size])
        list.append((line[::-1]+line[1:]).center(4*n-3, '-'))
    print('\n'.join(list[::-1]+list[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

"""Another solution"""

def print_rangoli(size):
    alphabet = [chr(i) for i in range(97, 123)]
    for i in range(size-1, -1, -1):
        print(('-'.join(alphabet[size-1:i:-1] + alphabet[i:size])).center(((size*4)-3), '-'))
    for i in reversed(range(size-1, 0, -1)):
        print(('-'.join(alphabet[size-1:i:-1] + alphabet[i:size])).center(((size*4)-3), '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
