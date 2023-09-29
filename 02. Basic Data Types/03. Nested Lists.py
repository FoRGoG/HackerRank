if __name__ == '__main__':
    dict = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in dict:
            dict[score].append(name)
        else:
            dict[score] = [name]
    list = []
    for i in dict:
        list.append([i, dict[i]])
    list.sort()
    result = list[1][1]
    result.sort()
    print(*result, sep='\n')