while True:

    try: 
        N = int(input())

        num_list = list(map(int, input().split()))
        diff_list = []

        #print(f"Num list = {num_list}")
        if len(num_list) == 1:
            print(1)

        for i in range(1, len(num_list)):

            #print(f"case {i}")

            first_part = num_list[:i]
            second_part = num_list[i:]

            #print(f"first_part = {first_part}")
            #print(f"second_part = {second_part}")

            first = sum(first_part)
            second = sum(second_part)

            diff = abs(first - second)
            diff_list.append(diff)

            #print(f"diff = {diff}")
            #print("")

        diff_list.sort()

        if len(diff_list) > 0:
            #print(f"Shortest diff = {diff_list[0]}")
            print(diff_list[0])

    except EOFError:
        break