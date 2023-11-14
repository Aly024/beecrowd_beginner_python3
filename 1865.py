N = int(input())

for i in range(N):

    hero, force = map(str, input().split())
    hero = hero.lower()
    if hero == "thor":
        print("Y")
    
    else:
        print("N")