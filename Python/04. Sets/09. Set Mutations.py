a = int(input())
A = set(map(int, input().split()))
N = int(input())
for i in range(N):
 first, second = input().split()
 if first == 'intersection_update':
   A.intersection_update(set(map(int, input().split())))
 elif first == 'update':
   A.update(set(map(int, input().split())))
 elif first == 'symmetric_difference_update':
   A.symmetric_difference_update(set(map(int, input().split())))
 else:
    A.difference_update(set(map(int, input().split())))

print(sum(A))
