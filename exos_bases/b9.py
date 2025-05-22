listeDicoDates =[
    { 'jour' : 4 , 'mois' : 'avril' , 'annee' : 2024} ,
    { 'jour' : 12 , 'mois' : 'juin' , 'annee' : 2023} ,
    { 'jour' : 22 , 'mois' : 'octobre' , 'annee' : 2025} ,
]

# construire et afficher des dates sous forme de chaines (via .format() )

for dicoDate in listeDicoDates :
    sDate = "{0} {1} {2}".format(dicoDate['jour'] , dicoDate['mois'] , dicoDate['annee'] )
    print("sDate=",sDate)

#recuperer et afficher date_et_heure (maintenant):
import datetime

d = datetime.datetime.now()
print("maintant=",d)    