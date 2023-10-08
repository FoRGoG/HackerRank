M = int(input())
second_line = set(map(int, input().split()))
N = int(input())
fourth_line = set(map(int, input().split()))
first_list = list(second_line.difference(fourth_line))
second_list = list(fourth_line.difference(second_line))
result = sorted(first_list + second_list)
for i in result:
    print(i)