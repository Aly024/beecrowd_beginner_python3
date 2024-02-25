#by chatgpt

n = int(input())
k = int(input())
a = []
for i in range(n):
    z = int(input())
    a.append(z)
a.sort(reverse=True)
count = 0

for i in range(n):
    count += 1
    if count == k:
        for j in range(i + 1, n):
            if a[i] != a[j]:
                break
            count += 1
        break

print(count)
