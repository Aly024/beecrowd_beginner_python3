#https://github.com/RatulAlMamun/URI-Solution/blob/master/01.%20Beginner/URI%202502%20-%20Deciphering%20the%20Encrypted%20Card.py

while True:
    try:
        C, N = map(int, input().split(" "))

        cipher = input().lower()

        decipher = input().lower()

        for i in range(N):
            sentence = input()
            
            for char in sentence:

                if char.isupper():
                    upper_case = True
                    char = char.lower()
                else:
                    upper_case = False

                if char in cipher:
                    index = cipher.index(char)
                    if upper_case:
                        print(decipher[index].upper(), end="")
                    else:
                        print(decipher[index], end="")

                elif char in decipher:
                    index = decipher.index(char) 
                    if upper_case:
                        print(cipher[index].upper(), end="")
                    else:
                        print(cipher[index], end="")
                else:
                    if upper_case:
                        print(char.upper(), end="")
                    else:
                        print(char, end="")
            print()
        print()

    except EOFError:
        break