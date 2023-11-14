msg = input()
ones = []

for c in msg:
    #print(c)

    if c == "1":
        ones.append(c)

#print(ones)
length = len(ones)
#print(length)
#print(msg[-1])

if (length % 2) != 0 and length > 0:
    msg+= "1"
else:
    msg+= "0"

print(msg)
    