listeVide=[]

listeInitiale=[1,2,3]

liste=listeInitiale
liste.append(4)
print("liste=",liste) # affiche [1,2,3,4]
print("liste=",liste)

print("premier élément:",liste[0]) # affiche 1
liste[0]=1.1
print("premier élément modifié:",liste[0]) # affiche 1.1
#liste[4]=5  --> IndexError: list assignment index out of range
print("dernier élément:",liste[-1]) # affiche 4 (dernier élément)


liste2 = [ "a" , "b" , "c" ]
del liste2[1] # suppression de l'élément d'indice 1 (0,1,2)
print("liste2=",liste2) # affiche [ 'a' , 'c' ]

liste3 = [ "rouge" , "vert" , "bleu" ]
liste3.remove("vert") # suppression de l'élément dont la VALEUR est "vert"
print("liste3=",liste3) # affiche [ 'rouge' , 'bleu' ]

liste4=[1,2,3,4];
liste4.reverse() # inverse l'ordre des éléments de la liste
print("liste4=",liste4) # affiche [ 4,3,2,1 ]

nbElements=len(liste4)
print("longueur (nbElements) de liste4=",nbElements) # affiche 4

liste5=['a' , 'b' , 'a' , 'b' , 'c' , 'a' ]
nbOccurencesDeA = liste5.count('a')
print("nbOccurences de 'a' dans liste5=",nbOccurencesDeA) # affiche 3

indiceBdansListe5= liste5.index('b') 
print("indiceBdansListe5",indiceBdansListe5) # 1 (premier trouvé)

indiceCdansListe5= liste5.index('c')
print("indiceCdansListe5",indiceCdansListe5) # 4 

autreListe = [ 'a' , 'b' , 'c1', 'd' , 'e']
autreListe.insert(3,'c2') #insertion avant l'élément actuel d'indice 3
                          #insertion du nouvel élément en pos 3 et en décalant la fin
print('autreListe apres insertion:' , autreListe)

#liste5.index('e') --> ValueError: 'e' is not in list

liste = [ 'a' , 'b', 'c' ]

#boucle sur indices:
for i in range(len(liste)) :
	print('i=',i,'liste[i]=',liste[i])
# i= 0 liste[i]= a
# i= 1 liste[i]= b
# i= 2 liste[i]= c


liste = [ 'a' , 'b', 'c' ]

#boucle sur valeur des éléments:
for val in liste :
	print(val)
# a 
# b
# c

#boucle sur indices et valeurs des éléments:
for tuple_indice_val in enumerate(liste) :
	print(tuple_indice_val , tuple_indice_val[0] , tuple_indice_val[1] )
# (0,'a') 0 a 
# (1,'b') 1 b
# (2,'c') 2 c

liste6 = [ 2 , 4 , 6 ]
refListe = liste6 # refListe référence la même liste que celle référencée par liste6
refListe[0]=2.2 # même effet que liste6[0] = 2.2
print("liste6=",liste6) # affiche [ 2.2 , 4 , 6 ]

liste7 = [ 1 , 3 , 5]
liste8 = liste7.copy() # copie/duplication d'une liste simple
liste8[0]=1.1
print("liste7=",liste7) # affiche [1, 3 , 5]
print("liste8=",liste8) # affiche [1.1, 3 , 5 ]

maPile = [ 1 , 2 ,  3 , 4]
dernierElementRetire  = maPile.pop(); print(dernierElementRetire); # 4
dernierElementRetire  = maPile.pop(); print(dernierElementRetire); # 3
print(maPile); # [ 1, 2 ]

troisCouleurs="rouge;vert;bleu" # grande chaîne de caractères avec sous parties séparées par ";"
listeCouleurs = troisCouleurs.split(";")
print("listeCouleurs=",listeCouleurs) # ['rouge', 'vert', 'bleu']

mesCouleurs=";".join(listeCouleurs) # transforme liste en chaîne de caractères
print("mesCouleurs=",mesCouleurs) # affiche la chaîne rouge;vert;bleu


liste10=[ 'a' , 'b' , 'c' ]
if 'a' in liste10 :
	print('liste10 comporte a')
else :
	print('liste10 ne comporte pas a')
	
if 'd' in liste10 :
	print('liste10 comporte d')
else :
	print('liste10 ne comporte pas d')	


'''
listeDeCouleurs =           [ 'rouge' , 'vert' , 'bleu' , 'noir' , 'blanc' ]
# indices ou positions :      0            1        2        3        4
print('la taille de liste de couleurs est ' , len(listeDeCouleurs) ) # affiche 5
print('la première couleur est ' , listeDeCouleurs[0] ) # affiche rouge
print('la couleurs du milieu est ' , listeDeCouleurs[2] ) # affiche bleu
print('la dernière couleur est ' , listeDeCouleurs[4] ) # affiche blanc
print('en dernier ' , listeDeCouleurs[ len(listeDeCouleurs)-1 ] ) #  blanc

print('plage 1 inclus à 3 exclus :' , listeDeCouleurs[1:3]) # ['vert', 'bleu']
print('plage début à 3 exclus :',listeDeCouleurs[:3]) # ['rouge', 'vert', 'bleu']
print('plage 2 inclus à fin  :',listeDeCouleurs[2:]) # ['bleu', 'noir', 'blanc']
'''