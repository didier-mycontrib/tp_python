x=0
while x <= 5 :
	print ('x=',x,'x*x=',x*x)
	x=x+1
print('suite apres la boucle')

listeCouleurs = [ "rouge" , "noir" ]
listeCouleurs.append("vert") # ajoute l'élément "vert" à la liste
listeCouleurs.append("bleu") # ajoute l'élément "bleu" à la liste
print("listeCouleurs=",listeCouleurs); # ['rouge', 'noir', 'vert', 'bleu']

#NB: un paquet de ligne de code encadré par ''' et '''
#    sont considérées comme 'en commentaire' et donc pas déclenchées/exécutées
'''
listeValeurs = []
valeurOuFin=input("val=")
while (valeurOuFin != 'fin' ) and (valeurOuFin != '' ):
	nouvelleValeur = float(valeurOuFin)
	listeValeurs.append(nouvelleValeur)
	valeurOuFin=input("val=")
print('listeValeurs=',listeValeurs)
'''

nom="toto"
nom=nom.upper() # retourne la chaine transformée avec des caractères majuscules
print(nom) # affiche TOTO

saisons = ["hiver" , "printemps" , "ete" , "automne" ] 
for i in range(len(saisons)) :
    s = saisons[i]
    saisons[i]=s.upper()
print(saisons)
