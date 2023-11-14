while True:
    try:
        N, D = map(int, input().split())
        result = []
        for i in range(D):
            
            date_str, *binary_values = input().split()

            if all(value == '1' for value in binary_values):
                result.append(date_str)


        if len(result) > 0:
            print(result[0])
        else:
            print("Pizza antes de FdI")

    except EOFError:
        break