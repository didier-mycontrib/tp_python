nbEssais=0
aDeviner=33
x=None
while x!=aDeviner :
    x=int(input("x="))
    nbEssais+=1
    if x > aDeviner :
        print("trop grand")
    elif x < aDeviner :
        print("trop petit")
    else:
        print("vous avez trouvé " + str(aDeviner) + " en " + str(nbEssais) + " essais")