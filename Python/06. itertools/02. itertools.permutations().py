from itertools import permutations

data, length = input().split()
result = sorted(list(permutations(data, int(length))))
for i in result:
    print(''.join(map(str, i)))
