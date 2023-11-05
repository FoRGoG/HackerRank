from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = list(product(a, b))
print(' '.join(map(str, result)))