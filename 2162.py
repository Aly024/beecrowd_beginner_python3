N = input()

landscape = list( map( int, input().split() ) )

result = 0

if len(landscape) > 2:

    for i in range(2,len(landscape)):

        if landscape[i-2] > landscape[i-1] and landscape[i-1] < landscape[i]:
            result = 1

        elif landscape[i-2] < landscape[i-1] and landscape[i-1] > landscape[i]:
            result = 1

        else:
            result = 0

else:
    if landscape[0] < landscape[1]:
        result = 1


print(result)
