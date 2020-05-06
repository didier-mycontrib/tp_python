a=15
print(type(a)) #affiche int ou <class 'int'>

s="abc"
print(type(s)) #affiche str ou <class 'str'>

x=2.4
print(type(x)) #affiche float ou <class 'float'>

c1=2+3j
print(type(c1)) #affiche complex ou <class 'complex'>

l1=['rouge' , 'vert' , 'bleu' ]
print(type(l1)) #affiche list ou <class 'list'>

ok=True
print(type(ok)) #affiche boolean ou <class 'bool'>

age=20
if age>=18:
    print('majeur pour age=',age)
    print('pas mineur')
print('suite dans tous les cas')

age=16
if age>=18:
	print('majeur pour age=',age)
else :
	print('mineur pour age=',age)
print('suite dans tous les cas')

age=30
if (age>=18) and (age<=42) :
	print('age entre 18 et 42 ans')
print('suite dans tous les cas')

age=16
if (age<18) or (age>=65) :
	print('enfant ou bien personne agée')
print('suite dans tous les cas')

listeDeCouleurs = [ 'rouge' , 'vert' , 'bleu' , 'noir' , 'blanc' ]
print('la taille de liste de couleurs est ' , len(listeDeCouleurs) )
print('la première couleur est ' , listeDeCouleurs[0] ) # affiche rouge
print('la couleurs du milieu est ' , listeDeCouleurs[2] )# affiche bleu
print('la dernière couleur est ' , listeDeCouleurs[4] )# affiche blanc
print('en dernier ' , listeDeCouleurs[len(listeDeCouleurs)-1] )#  blanc

seq=1,2,3
print('sequence 1, 2 , 3',seq, type(seq)) # s'affiche comme (1 , 2 , 3)

print('range(4)=de 0 à 3<4 =',list(range(4))) # affiche [ 0,1,2, 3 ]
print('range(3,6)=de 3 à 5<6 = ',list(range(3,6))) # affiche [ 3, 4 , 5 ]
print('range(4-1,0-1,-1)= séquence inversée = ',list(range(3,-1,-1))) # affiche [ 3, 2 , 1 , 0 ]

#indicesDe0a3= 0,1,2,3
indicesDe0a3= range(4) # range(4) construit 0, 1, 2, 3
for i in indicesDe0a3 :
	print("i=",i)
print('suite apres la boucle')

print('boucle de 2 à 8<9 par pas de 2 soit de 2 en 2 :');
for i in range(2,9,2) :
	print("i=",i)
print('suite apres la boucle')

joursDeLaSemaine = ['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche']
# la liste (ou tableau) joursDeLaSemaine comporte 7 éléments dont les positions/indices vont de 0 à 6
for jour in joursDeLaSemaine :
	print(jour,'est un element de joursDeLaSemaine')
print('suite apres la boucle')

#nbJoursDansUneSemaine=7
nbJoursDansUneSemaine=len(joursDeLaSemaine) # la fonction len() retourne la taille/longueur (length en englais)
for i in range(nbJoursDansUneSemaine) :
	print("i=",i,"jour=",joursDeLaSemaine[i])
print('suite apres la boucle')

liste =[ 10 , 40 , 30 , 50 , 20 ]
somme=0;
taille=len(liste)
for valElt in liste :
	somme=somme + valElt
moyenne=somme/taille;
print('somme=',somme) # affiche 150
print('moyenne=',moyenne) # affiche 30
	

