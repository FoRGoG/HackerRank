from collections import Counter

number_of_shoes = int(input())
list_of_all_shoes = list(map(int, input().split()))
count_shoes = Counter(list_of_all_shoes)
money_earned = 0
for i in range(int(input())):
    size, prise = map(int, input().split())
    if size in count_shoes.keys():
        if count_shoes[size] != 0:
            count_shoes[size] -= 1
            money_earned += prise
        else:
            money_earned += 0
print(money_earned)
