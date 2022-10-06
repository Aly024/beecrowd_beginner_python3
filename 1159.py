while True:

    x = int(input())

    if x == 0:
        break

    else:

        even_num = []
        count = 0

        while (count<5):

            z = x
            if z%2 ==0:
                even_num.append(z)
                count += 1
            x += 1

        print(sum(even_num))