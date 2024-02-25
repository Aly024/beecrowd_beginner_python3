L = input()
pos = ord(L) - ord("A") + 1
print(pos)
'''
Code form ChatGPT
# Get the uppercase letter as input
letter = input("Enter an uppercase letter ('A' - 'Z'): ")

# Check if the input is a single uppercase letter
if len(letter) == 1 and 'A' <= letter <= 'Z':
    # Convert the letter to its corresponding position in the alphabet
    position = ord(letter) - ord('A') + 1

    # Print the result
    print(f"The position of {letter} in the alphabet is: {position}")
else:
    print("Invalid input. Please enter a single uppercase letter.")
'''