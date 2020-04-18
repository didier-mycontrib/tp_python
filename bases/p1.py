a=2  # nomVariable=valeur_a_affecter
print(a) #affiche la valeur de a (ici 2)
b=a*3+4  # variableResultat = expression d'un calcul
c=a+b
print("b=",b,"c=",c)#affiche plusieurs choses en les séparant par des espaces
                    #affiche ici b= 10 c= 12
					
prenom = "alex"  # une chaine de caractères est délimitée en python
nom = 'Therieur' # par des " " ou des ' '
nomComplet = prenom + ' ' + nom # concatenation (ajout bout à bout)
print (nomComplet) # affiche alex Therieur
 					
# input('texte question') demande à saisir/renseigner une valeur					
age = input ("quel est ton age ? ") 
print ('age renseigné:' , age);  # affichera la valeur choisie/précisée .	

a=input('a:') # exemple a: 2 et a vu comme '2'
b=input('b:') # exemple b: 3 et b vu comme '3'
c=a+b # '2' + '3' = '23'
print('c=a+b=',c) # affiche par exemple c=a+b= 23

a=float(input('a:')) # exemple a: 2 et a vu comme 2.0
b=float(input('b:')) # exemple b: 3 et b vu comme 3.0
c=a+b # 2.0 + 3.0 = 5.0 = 5
print('c=a+b=',c)# affiche par exemple c=a+b= 5

# a faire en exercice:
x=float(input("x="))
y=float(input("y="))
moyenne=(x+y)/2;
print("moyenne=",moyenne)		
					