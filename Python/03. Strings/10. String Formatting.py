def print_formatted(number):
    space = len(bin(n)[2:])
    for i in range(1, number+1):
        print (str(i).rjust(space, ' '),
               str(oct(i)[2:]).rjust(space, ' '),
               str(hex(i)[2:].title()).rjust(space, ' '),
               str(bin(i)[2:]).rjust(space, ' '))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

'''Another solution'''

def print_formatted(number):
    width = len(str(bin(number)[2:]))
    for i in range(1, number+1):
        print(f'{str(i).rjust(width)} '
              f'{oct(i)[2:].rjust(width)} '
              f'{str(hex(i)[2:]).upper().rjust(width)} '
              f'{bin(i)[2:].rjust(width)}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
