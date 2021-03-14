from Repositories.utils import get_cursor
from dbpath import DB_PATH
import sqlite3

def get_interventions():
    cursor = get_cursor()
    query = "SELECT * FROM intervention"
    return cursor.execute(query).fetchall()


def get_by_id(idInter):
    cursor = get_cursor()
    statement = "SELECT * FROM intervention WHERE idIntervention = ?"
    return cursor.execute(statement, [idInter]).fetchone()

def add_intervention(intervention):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    statement = "INSERT INTO intervention (idTechnicien,idClient, piece, probleme) VALUES (?,?,?,?)"
    try:
        cur.execute(statement, [intervention.idTech, intervention.idClient, intervention.piece, intervention.probleme])
        con.commit()
        return 1       
    except:
        return 0
