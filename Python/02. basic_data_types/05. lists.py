if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        result = input().split()
        if result[0] == 'insert':
            list.insert((int(result[1])), (int(result[2])))
        elif result[0] == 'print':
            print(list)
        elif result[0] == 'remove':
            list.remove((int(result[1])))
        elif result[0] == 'append':
            list.append((int(result[1])))
        elif result[0] == 'sort':
            list.sort()
        elif result[0] == 'pop':
            list.pop()
        elif result[0] == 'reverse':
            list.reverse()

