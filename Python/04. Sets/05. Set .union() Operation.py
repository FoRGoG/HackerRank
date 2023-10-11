english_newspaper_people = int(input())
numbers_english_people = set(map(int,input().split()))
french_newspaper_people = int(input())
numbers_french_people = set(map(int,input().split()))
print(len(numbers_english_people | numbers_french_people))

'''another print variation'''

print(len(numbers_english_people.union(numbers_french_people)))