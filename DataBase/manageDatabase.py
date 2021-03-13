import sqlite3
import os
from dbpath import DB_PATH
DATABASE_NAME = "easySAV.db"


def get_db():
    connexion = sqlite3.connect(DB_PATH)
    return connexion


def create_databse():
    try:
        os.remove(DB_PATH)

        # Création des tables
        tables = [
            """
                          CREATE TABLE IF NOT EXISTS intervention(
                              idIntervention INTEGER PRIMARY KEY AUTOINCREMENT,
                              idTechnicien INTEGER NOT NULL,
                              idClient INTEGER NOT NULL,
                              piece TEXT NOT NULL,
                              probleme TEXT NOT NULL      
                          )
                      """,
            """
                CREATE TABLE IF NOT EXISTS technicien(
                    idTechnicien INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    prenom TEXT NOT NULL
                )
            """

        ]
        db = get_db()
        cursor = db.cursor()             
        for table in tables:
            cursor.execute(table)

        # Création des techniciens

        techniciens = [
            ("Leclercq", "Anthony"),
            ("Koffi", "Yahse Josias"),
            ("Lecomte", "Antoine")
        ]

        cursor.executemany("INSERT INTO technicien (nom, prenom) VALUES (?, ?)", techniciens)

        # Création des interventions

        interventions = [
            (1,2,"Carte Graphique", "La carte graphique a cramé"),
            (2,1, "Ecran", "L'écran ne fonctionne plus"),
            (3,3,"Alimentation", "L'alimentation à cramé"),
            (2,3,"Carte Réseau", "Pièce défaillante"),
            (3,2,"Clavier", "Manque de lettres")
        ]

        cursor.executemany("INSERT INTO intervention (idTechnicien,idClient,piece, probleme) VALUES (?, ?, ?,?)", interventions)

        db.commit()

    except Exception as exception:
        print(exception)
