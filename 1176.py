T = int(input())

for i in range(T):

    N = int(input())

    sequence = [0,1]
    #result = 0

    for i in range(N):

        #print(sequence)
        result = int(sequence[-1] + sequence[-2])
        #print(result)
        sequence.append(result)
    
    print(f"Fib({N}) = {sequence[N]}")