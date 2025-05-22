liste = [ "rouge" , "vert" , "bleu" , "rouge" , "vert"]
colorSet = set(liste)
print("colorSet=",colorSet , " type = " , type(colorSet));

colorSet2 = { "jaune" , "vert" , "orange"}
allColorSet = colorSet.union(colorSet2)
print("allColorSet=",allColorSet)

jourSet = { "erreur", "lundi" , "mardi" , "mercredi" , "jeudi"}
jourSet.discard("erreur")
jourSet.add("vendredi")
print("jourSet=",jourSet)
jourSet.update({"samedi" , "dimanche"})
print("jourSet=",jourSet)
jourSet.clear()
print("jourSet=",jourSet)