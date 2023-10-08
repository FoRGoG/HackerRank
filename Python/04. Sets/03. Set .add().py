s = set()
N = int(input())
while N > 0:
    stamps= input()
    s.add(stamps)
    N -= 1
print(len(s))