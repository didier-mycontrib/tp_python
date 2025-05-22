nomFichiers=[ "fichierA.txt" , "configB.json" , "b8.py" ]
# boucler sur chaque nom complet de fichier
# et afficher séparément nom et extension 
for nomFic in nomFichiers:
    posPoint=nomFic.find('.')
    print("nomFic=",nomFic,"posPoint=",posPoint)
    nom=nomFic[0:posPoint] # [0,posPoint[
    extension=nomFic[posPoint+1:len(nomFic)] 
    print("nom=",nom,"extension=",extension)
