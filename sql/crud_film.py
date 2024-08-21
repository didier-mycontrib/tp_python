import json
from datetime import datetime
import mysql.connector
# python -m pip install mysql-connector-python

connection_params = {
    'host': "localhost",
    'user': "root",
    'password': "root",
    'database': "filmDB",
}

#se connecter à la base de donnees et utiliser la connexion 
#** operator to unpack dictionaries directly into keyword arguments of a function
with mysql.connector.connect(**connection_params) as db  : 

    #insertion de donnees:
    insertRequest = """insert into film
             (titre, dateSortie)
             values (%s, %s)"""  # all parameter marker must be %s (as ?), not %d
    params = ("filmXyz", datetime.now())
    with db.cursor() as c:
        c.execute(insertRequest, params)
        db.commit()
        print("id (auto incrémenté) du dernier film ajouté :", c.lastrowid)


    # requete sql select ...
    selectRequest = "select id, titre, dateSortie from film"
    columnNamesTuple = ("id", "titre", "dateSortie")

    with db.cursor() as c:
        c.execute(selectRequest)
        resultats = c.fetchall()
        print("Nombre de lignes sélectionnées/récupérées :", c.rowcount) 
        for film in resultats:
            #print(film) # film is a tuple (immutable list of field values)
            filmAsDict = {columnNamesTuple[i] : film[i] for i, _ in enumerate(columnNamesTuple)}
            print(filmAsDict)
            
        
    #fermeture automatique de la connexion en fin de bloc with db:
