s1="Hello"
s2=' World'
s3=s1+s2 #concatenation
print(s3) # Hello World

s4='''ile de
france'''
print(s4) # affiche une chaine multi-lignes

s5="Bonjour"
premierCaractere=s5[0]
print(premierCaractere) # B

dernierCaractere=s5[-1]
print(dernierCaractere) # r

# [i,j] means .substring(i,j) included i and excluding j

troisPremiersCaracteres=s5[0:3]# s5[0:3] means s5[0:3[ !!!
print(troisPremiersCaracteres) # Bon

n=len(s5) # length of string (7)

troisDerniersCaracteres=s5[n-3:n]# s5[n-3:n] means s5[n-3:n[ !!!
print(troisDerniersCaracteres) # our

s6=" Ile De France "
s6Bis=s6.strip() #like trim of other language --> supprime espaces inutiles
                 #au début ou à la fin
print(s6Bis) # "Ile De France"

s7="Mont Saint Michel"
s7Maj = s7.upper(); print(s7Maj) # MONT SAINT MICHEL 
s7Min = s7.lower(); print(s7Min) # mont saint michel

s7="Mont Saint Michel"
s7Bis=s7.replace(' ','-'); # replace substring with another string
print(s7Bis) # Mont-Saint-Michel

s8="partie1;partie2;partie3"
listeParties=s8.split(';')
print(listeParties) # ['partie1', 'partie2', 'partie3']

s9="un deux trois"
if "deux" in s9 :
	print("s9 comporte deux")
else :
	print("s9 ne comporte pas deux")

#il existe aussi le test if "deux" not in s9 

nom="toto"
age=30
taille=1.80
#.format remplace {0} , {1} , {2} , ... par les 1er,2eme,3eme arguments
description="{0} a {1} an(s) et mesure {2} m".format(nom,age,taille)
print(description) # toto a 30 an(s) et mesure 1.8 m

#caractères spéciaux : \n = new line , \t = tabulation , ...
#escape : \\ means \ 

s10="\tHello" ; print(s10); #      Hello
s11="surLigne1\nsurLigne2" ; print(s11); 
# surLigne1
# surLigne2

s12="dupond";
s12Bis=s12.capitalize() # transforme première lettre en Majuscule
print(s12Bis); # Dupond

fileName="p2.py"
dotIndex = fileName.find(".") 
# .index() retourne position de la chaine recherchée et erreur si pas trouvée
# .find() retourne position de la chaine recherchée et -1 si pas trouvée
print("position . =" , dotIndex) # 2

s13="phrase finissant par un point."
if s13.endswith(".") :
	print("s13 se termine par '.' ")
	
s14="123"
if s14.isdigit() :
	print("s14 ne comporte que des caractères numériques ")
	
