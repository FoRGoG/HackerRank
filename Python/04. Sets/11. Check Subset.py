for i in range(1, int(input())+1):
    number_elements_a = int(input())
    set_a = set(map(int, input().split()))
    number_elements_b = int(input())
    set_b = set(map(int, input().split()))
    print(set_a < set_b)
