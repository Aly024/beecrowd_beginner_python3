while True:

    try:

        N = int(input())

        if N > 0:
            print("vai ter duas!")
        else:
            print("vai ter copa!")

    except EOFError:
        break