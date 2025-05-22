ensembleVide={}

#dans un ensemble, les éléments ne sont pas ordonnés (sans index stables)
ensembleDeFruits={"apple", "banana", "cherry"} 

print("ensembleDeFruits=",ensembleDeFruits) #  {'banana', 'cherry', 'apple'}

for f in ensembleDeFruits:
  print(f)
#banana
#cherry
#apple

#NB: une fois qu'un ensemble a été créé/initialisé , on ne peut pas modifier
# ses éléments mais on peut ajouter un nouvel élément via .add()
# ou bien de nouveaux éléments via .update()

ensembleDeFruits.add("orange") # ajout (sans notion d'ordre)
print(ensembleDeFruits) # {'apple', 'orange', 'banana', 'cherry'}

ensembleDeFruits={"apple", "banana", "cherry"}
ensembleDeFruits.update({"orange" , "peach"}) # ajout de plusieurs éléments
print(ensembleDeFruits) # {'apple', 'peach', 'banana', 'orange', 'cherry'}

ensembleDeFruits={"apple", "banana", "cherry"}
ensembleDeFruits.remove("banana") # supprime un élément s'il existe , erreur sinon
print(ensembleDeFruits)  # {'cherry', 'apple'}
ensembleDeFruits.discard("banana") # supprime un élément s'il existe toujours sans erreur 

ensembleDeFruits.clear() # vide l'ensemble
print(ensembleDeFruits)  # {}

set1 = {"a", "b" , "c"}
set2 = {"d", "e", "f"}

set3 = set1.union(set2)
print(set3) # {'b', 'd', 'a', 'e', 'c', 'f'}

set4 = {"a", "b" , "c" , "d"}
set5 = {"c", "d" , "e" , "f"}

set6 = set4.intersection(set5)
print(set6) # {'d', 'c'}

#il existe également .isdisjoint() , .issubset() , .difference() , ...

# transformations de set en liste , tuple et vice versa
set1 = {"a", "b" , "c"  }
listeFromSet1 = list(set1)
print("listeFromSet1",listeFromSet1,type(listeFromSet1))



tuple1 = ("a", "doublon", "b" , "c" , "doublon")
setFromTuple1 = set(tuple1)
print("setFromTuple1 =", setFromTuple1 ,type(setFromTuple1))

tuple2 = ("a", "b" , "c"  )
listeFromTuple2 = list(tuple2)
print("listeFromTuple2",listeFromTuple2,type(listeFromTuple2))