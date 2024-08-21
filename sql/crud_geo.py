import json
import mysql.connector
# python -m pip install mysql-connector-python

connection_params = {
    'host': "localhost",
    'user': "root",
    'password': "root",
    'database': "geoDB",
}

#se connecter à la base de donnees et utiliser la connexion 
#** operator to unpack dictionaries directly into keyword arguments of a function
with mysql.connector.connect(**connection_params) as db  : 

    #insertion de donnees:
    insertRequest = """insert into departement
             (numero, nom, population, superficie, prefecture)
             values (%s, %s, %s, %s , %s)"""  # all parameter marker must be %s (as ?), not %d
    params = ("57", "Moselle", 0, 0 , "Metz")
    with db.cursor() as c:
        c.execute(insertRequest, params)
        db.commit()
        print("Nombre de lignes insérées :", c.rowcount)

    #mise à jour de donnees:
    updateRequest = """update departement
             set population=%s, superficie=%s
             where numero=%s""" 
    params = (1049942, 6216 ,"57")
    with db.cursor() as c:
        c.execute(updateRequest, params)
        db.commit()
        print("Nombre de lignes modifiees :", c.rowcount)

    # requete sql select ...
    selectRequest = "select numero, nom, population, superficie, prefecture from departement"
    columnNamesTuple = ("numero", "nom", "population", "superficie", "prefecture")

    with db.cursor() as c:
        c.execute(selectRequest)
        resultats = c.fetchall()
        print("Nombre de lignes sélectionnées/récupérées :", c.rowcount) 
        for departement in resultats:
            #print(departement) # department is a tuple (immutable list of field values)
            depAsDict = {columnNamesTuple[i] : departement[i] for i, _ in enumerate(columnNamesTuple)}
            print(depAsDict)
            depAsJsonString = json.dumps(depAsDict);
            #print (depAsJsonString)
            
    #suppression de donnees:
    deleteRequest = """delete from departement
             where numero=57""" 
    with db.cursor() as c:
        c.execute(deleteRequest)
        db.commit()
        print("Nombre de lignes supprimées :", c.rowcount) 
        
    #fermeture automatique de la connexion en fin de bloc with db:
