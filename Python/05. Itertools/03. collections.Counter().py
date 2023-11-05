from collections import Counter

number_of_shoes = int(input())
list_of_all_shoes = list(map(int,input().split()))[0:number_of_shoes]
count_shoes = Counter(list_of_all_shoes)
print(count_shoes)
number_of_customers = int(input())
for i in range(number_of_customers):
    money_earned = 0

