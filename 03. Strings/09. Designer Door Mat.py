N, M = map(int,input().split())

#Top lines
for i in range(1, N, 2):
    print(('.|.'*i).center(M, '-'))

#Middle line
print('WELCOME'.center(M, '-'))

#Bottom lines
for i in reversed(range(1, N, 2)):
    print(('.|.' * i).center(M, '-'))
