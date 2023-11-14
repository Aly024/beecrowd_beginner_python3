N = int(input())
N = str(N)
word = []
for i in N:
    word.append(i)

word.reverse()
print("".join(word))