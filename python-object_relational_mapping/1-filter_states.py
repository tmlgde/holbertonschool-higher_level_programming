#!/usr/bin/python3
"""List all states starting with N from hbtn_0e_0_usa database"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]      # ex: python_user
    password = sys.argv[2]      # ex: password
    db_name = sys.argv[3]       # ex: hbtn_0e_0_usa

    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Création du curseur et exécution de la requête
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Affichage des résultats
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Fermeture propre
    cur.close()
    db.close()
