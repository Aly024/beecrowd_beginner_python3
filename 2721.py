names = ["Dasher", "Dancer", "Prancer", "Vixen", "Comet", "Cupid", "Donner", "Blitzen", "Rudolph"]
snowballs = list(map(int, input().split()))
#print(snowballs)
total = sum(snowballs)
#print(total)

result = total - (9*int(total/9))
#print(result)

if result == 0:
    print(names[8])
else:
    print(names[result-1])