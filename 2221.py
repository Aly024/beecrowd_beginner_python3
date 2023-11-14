tc = int(input())

for i in range(tc):
        

    bonus = int(input())

    A1, D1, L1 = map(int, input().split())
    A2, D2, L2 = map(int, input().split())

    def value(A, D, L):
        val = (A + D )/2

        if L%2 == 0:
            val += bonus

        return val


    val1 = value(A1,D1,L1)
    val2 = value(A2,D2,L2)

    #print(val1)
    #print(val2)

    if val1 == val2:
        print("Empate")
    elif val1 > val2:
        print("Dabriel")
    elif val1< val2:
        print("Guarte")

