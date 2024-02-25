N = int(input())
searched = []
for i in range(N):
    searched.append(input())

Q = int(input())
word = []
for j in range(Q):
    word.append(input())

for j in range(Q):
    count = 0
    longest_word = ""
    for i in range(N):
        X = word[j]
        Y = searched[i]
        if X in Y and X[0] == Y[0] and X[1] == Y[1]:
            count += 1
            #print(f"{word[j]} {searched[i]} {count}")
            if ( len(searched[i]) > len(searched[i-1]) ):
                longest_word = searched[i]
    if count == 0:
        print("-1")
    else:
        print(f"{count} {len(longest_word)}")

'''
maratonaicpc
maraton
programacao
progress
inputs
'''

'''
marat
programacao
outputs
'''