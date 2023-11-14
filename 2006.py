tea_type = int(input())

contestant = list(map(int,input().split()))

result = 0

for item in contestant:

    if item == tea_type:
        result += 1

print(result)