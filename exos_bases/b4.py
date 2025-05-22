values = [ -2 , -7 , 2 , 8 , -9 , 10 , 1 , 3 , -3 , 5]
dicoStats = { 'nb_positif' : 0 , 'nb_negatif' : 0 ,
             'nb_pair' : 0 , 'nb_impair' : 0 ,
             'taille' : 0 , 'somme' : 0}

dicoStats['taille']=len(values)
for v in values:
    dicoStats['somme']+=v
    if v>=0 :
        dicoStats['nb_positif']+=1
    else:
        dicoStats['nb_negatif']+=1
    if v%2==0 :
        dicoStats['nb_pair']+=1
    else:
        dicoStats['nb_impair']+=1

print("dicoStats=" , dicoStats)