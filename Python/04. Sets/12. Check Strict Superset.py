"""My own summer (solution)"""
main_set = set(map(int, input().split()))
number_sets = int(input())
new_list = list()
for i in range(1, number_sets+1):
    other_set = set(map(int, input().split()))
    result = other_set < main_set
    new_list.append(result)
print(False if False in new_list else True)