glass = list(map(int, input().split()))

for i, value in enumerate(glass):
    if value == 1:
        print(i + 1)
