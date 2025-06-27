#!/usr/bin/python3

"""Script that lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connexion à la base de données
    db = MySQLdb.connect(
        host="127.0.0.1",  # ou "localhost" si le socket fonctionne
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Création du curseur
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Récupération et affichage des résultats
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()
