#p4.py : fonctions

#fonction basique sans paramètre retournant une valeur fixe:
def genererMessageSalutation():
	message="bonjour"
	return message
	
#fonction/procedure basique ne retournant aucune valeur
#mais exécutant une action:	
def saluer():
	salutation=genererMessageSalutation() #appel de sous-fonction
	print(salutation)	
	
saluer() #l'appel de la fonction déclenche l'affichage de bonjour

#fonction multiplier avec 2 parametres formels a et b
def multiplier(a,b):
	return a*b
	
x=4; y=5;
res = multiplier(x,y); # appel de la fonction multiplier en passant
                       # les valeurs des paramètres effectifs x et y
					   # lors de l'appel a est une copie de x
					   # et b est une copie de y

print("res=",res) # affiche res=20

