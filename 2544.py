#https://github.com/mcavalca/uri-python/blob/master/2544.py

while True:
    try:
        n = int(input())
        i = 0
        while(n > 1):
            n //= 2
            i += 1
        print(i)
    except EOFError:
        break