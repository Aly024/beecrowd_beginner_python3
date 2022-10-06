while True:

    X = int(input())
    
    if X == 0:
        break
    
    output = ""
    count = 1
    for i in range(1,X+1):
        output += str(count) + " "
        count += 1

    print(output[:-1])
