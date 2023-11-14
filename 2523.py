while True:
    try:

        msg = input()

        count = int(input())
        count_list = list(map(int, input().split()))
        #print(count_list)

        output = []

        for num in count_list:
            #print(msg[num-1])
            output.append(msg[num-1])

        result = "".join(output)
        print(result)

    except EOFError:
        break