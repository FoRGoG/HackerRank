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