N = int(input())

sequence = [0,1]
result = 0

for i in range(N-2):

    #print(sequence)
    result = int(sequence[-1] + sequence[-2])
    #print(result)
    sequence.append(result)

print(sequence)
print(sequence[:N])
print(' '.join(map(str,sequence)))