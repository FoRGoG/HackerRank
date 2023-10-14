K = int(input()) # members per group
unordered_room_numbers = list(map(int, input().split()))
room_numbers = set(unordered_room_numbers)
sum1 = sum(unordered_room_numbers)
sum2 = sum(room_numbers)
result = sum2*K - sum1
result1 = result // (K -1)
print(result1)