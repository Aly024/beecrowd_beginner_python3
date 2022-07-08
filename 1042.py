# https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/#:~:text=In%20C%2B%2B%2FC%20user,one%20line%20by%20two%20methods.&text=Using%20split()%20method%20%3A,input%20by%20the%20specified%20separator.

val = list(map(int, input().split()))

val2 = val.copy()

val.sort()

for i in range(len(val)):
    print(val[i])

print()

for i in range(len(val2)):
    print(val2[i])