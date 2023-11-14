case_no = 1
while True:
    try:

        N = int(input())
        i = 0
        ans = []
        while i != N+1:

            if i == 0:
                ans.append(i)

            else:
                for j in range(i):
                    ans.append(i)

            i+=1

        if len(ans) == 1:
            numbers = 'numero'
        else:
            numbers = 'numeros'
            
        no_of_items = len(ans)
        print(f"Caso {case_no}: {no_of_items} {numbers}")
        print(*ans)
        print()
        case_no += 1 

    except EOFError:
        break