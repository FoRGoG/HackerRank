if __name__ == '__main__':
    n = int(input())
    arr = list(sorted(set((map(int, input().split())))))
    arr1 = arr[:n]
    print(arr1[-2])

"""Clear solution"""
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr))[-2])