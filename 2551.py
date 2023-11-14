while True:
    try:
        N = int(input())

        update_speed = 0

        for i in range(N):

            time, dist = map(int, input().split())
            speed = dist/time

            if speed > update_speed:
                update_speed = speed
                print(i+1)
    
    except EOFError:
        break