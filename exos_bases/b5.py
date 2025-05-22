dicoProduits={
    'fruit' : [ "banane" , "orange" , "pomme" ] ,
    'legume' : [ "carotte" , "choux" , "tomate"],
    'divers' : [ 'stylo' , 'cahier']
}
#supprimer la categorie de produits qui ne se mange pas
del dicoProduits["divers"]

#afficher le dictionnaire complet:
print("dicoProduits=",dicoProduits)

#afficher la liste des clefs (categories):
print("categories de produits=",list(dicoProduits.keys()))

#afficher la liste des fruits:
print("liste des fruits=",dicoProduits['fruit'])

# transformer les noms des produits en majuscule
for categorie in dicoProduits :
    for i in range(len(dicoProduits[categorie])) :
        prod = dicoProduits[categorie][i]
        prod=prod.upper()
        dicoProduits[categorie][i]=prod
      

#ré-afficher le dictionnaire:
print("dicoProduits=",dicoProduits)        