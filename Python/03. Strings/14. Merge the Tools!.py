def merge_the_tools(string, k):
    result = list()
    result1 = list()
    ln = len(string)
    for i in range(0, ln, k):
        result.append(string[i:i+k])
    for word in result:
        sub = list()
        for i in word:
            if i not in sub:
                sub.append(''.join(i))
        result1.append(''.join(sub))
    for i in result1:
        print(i)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
