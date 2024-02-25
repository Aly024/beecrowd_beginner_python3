# accepted code
#https://github.com/mcavalca/uri-python/blob/master/2653.py
#Explanation by chatgpt
'''l = set(l): Converts the list l into a set. 
A set is an unordered collection of unique elements, so duplicate entries in the list will be removed.

print(len(l)): Prints the length of the set l. 
The length of a set is the number of unique elements in it. 
Therefore, this line prints the number of unique inputs entered by the user before encountering an EOFError.'''

l = []

while True:
    try:
        l.append(input())
        
    except EOFError:
        break
        
l = set(l)
print(len(l))



# my code
'''
count = 0
jewel = []

while True:
    try:
        N = input()

        if N in jewel:
            count += 1
            jewel.append(N)
        else:
            jewel.append(N)
        

    except EOFError:
        break

print(count)

'''