from Repositories.utils import get_cursor


def get_interventions():
    cursor = get_cursor()
    query = "SELECT * FROM intervention"
    return cursor.execute(query).fetchall()


def get_by_id(idInter):
    cursor = get_cursor()
    statement = "SELECT * FROM intervention WHERE idIntervention = ?"
    return cursor.execute(statement, [idInter]).fetchone()


def insertIntervention(intervention):
    cursor = get_cursor()
    statement = ""
