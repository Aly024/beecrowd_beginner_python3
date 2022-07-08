word1 = input()
word2 = input()
word3 = input()

#If vertebrado is selected
if ( word1 == "vertebrado" and word2 == "ave"):
    if word3 == "carnivoro":
        print("aguia")
    if word3 == "onivoro":
        print("pomba")

if ( word1 == "vertebrado" and word2 == "mamifero"):
    if word3 == "herbivoro":
        print("vaca")
    if word3 == "onivoro":
        print("homem")

#If invertebrado is selected
if ( word1 == "invertebrado" and word2 == "inseto"):
    if word3 == "hematofago":
        print("pulga")
    if word3 == "herbivoro":
        print("lagarta")

if ( word1 == "invertebrado" and word2 == "anelideo"):
    if word3 == "hematofago":
        print("sanguessuga")
    if word3 == "onivoro":
        print("minhoca")