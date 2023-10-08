n = int(input())
s = set(map(int, input().split()))
c = int(input())
for i in range(c):
    result = input().split()
    if 'pop' in result:
        s.pop()
    elif 'remove' in result:
        s.remove(int(result[1]))
    elif 'discard' in result:
        s.discard(int(result[1]))
print(sum(s))
