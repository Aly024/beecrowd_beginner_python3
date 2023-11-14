#https://github.com/mcavalca/uri-python/blob/master/2708.py

tourist = 0
jeep = 0

while True:
    user_input = input().split()

    if user_input[0] == "ABEND":
        break

    if user_input[0] == "SALIDA":
        jeep += 1
        tourist += int(user_input[1])

    if user_input[0] == "VUELTA":
        jeep -= 1
        tourist -= int(user_input[1])

print(tourist)
print(jeep)