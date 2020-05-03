dictionnaireVide={}
dictionnaire2 = dict()

#un dictionnaire python est une table d'association (Map)
#(ensemble de couples (clef,valeur))
#La syntaxe d'un dictionnaire python est très proche de JSON (javascript object notation)
dictionnaireCouleurs={
"red":"#ff0000",
"green":"#00ff00",
"blue":"#0000ff"
} 

rgbRed=dictionnaireCouleurs["red"];
print("rgbRed=",rgbRed); # #ff0000
dictionnaireCouleurs["red"]="#FF0000"; # change value 
print(dictionnaireCouleurs["red"]); # #FF0000

rgbGreen=dictionnaireCouleurs.get("green");
print("rgbGreen=",rgbGreen); # #00ff00

dictionnaireCouleurs["black"]="#000000"; # add new key and value 
print(dictionnaireCouleurs["black"]); # #000000

dictionnaireCouleurs.update({"white":"#FFFFFF"}); # add new {key : value } pair
print(dictionnaireCouleurs["white"]); # #FFFFFF

dictionnaireCouleurs.update({"white":"#ffffff" , "yellow" : "#ffff00"}); # fusionner autre dictionnaire
print(dictionnaireCouleurs["yellow"]); # #ffff00

del dictionnaireCouleurs["white"]; #ou bien dictionnaireCouleurs.pop("white")
print(dictionnaireCouleurs); # {'red': '#FF0000', 'green': '#00ff00', 'blue': '#0000ff', 'black': '#000000', 'yellow': '#ffff00'}

dicoPers= { "nom" : "Bon" , "age" : 45 }
print("nom=" + dicoPers.get("nom")); # Bon
print("nom=" + dicoPers.get("prenom","prenomParDefaut")); # prenomParDefaut

dicoPers= { "nom" : "Bon" , "age" : 45 }
for key in dicoPers :
	print(key)
# nom
# age

dicoPers= { "nom" : "Bon" , "age" : 45 }
for clef in dicoPers.keys() :
	print(clef)
# nom
# age

for val in dicoPers.values() :
	print(val)
# Bon
# 45

for clef,val in dicoPers.items() :
	print(clef,val)
# nom Bon
# age 45

dicoPers= { "nom" : "Bon" , "age" : 45 }
print("nbAssociations=" , len(dicoPers)) # 2
dicoDuplique=dicoPers.copy(); #ou bien dicoDuplique=dict(dicoPers);
dicoDuplique["age"]=30
print(dicoPers) # { "nom" : "Bon" , "age" : 45 }
print(dicoDuplique) # { "nom" : "Bon" , "age" : 30 }

dicoDuplique.clear() # vide le contenu du dictionnaire

if "nom" in dicoPers:
	print("dicoPers comporte la clef nom")
else :
	print("dicoPers ne comporte pas la clef nom")
	
#NB: au sein d'un dictionnaire une valeur peut être 
#une liste ou un dictionnaire imbriqué:
dicoPers={
  "nom" : "Bon" ,
  "age" : 45 ,
  "fou" : False,
  "adresse" : {
         "rue" : "12 rue elle",
		 "codePostal" : "75008",
		 "ville" : "Paris" 
		 } ,
   "sports" : [ "vélo" , "foot" ]
 }
print("dicoPers très proche du format JSON:" , dicoPers);


