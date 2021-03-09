from Repositories.utils import get_cursor


def get_techniciens():
    cursor = get_cursor()
    query = "SELECT * FROM technicien"
    return cursor.execute(query).fetchall()


def get_by_id(idTech):
    cursor = get_cursor()
    statement = "SELECT * FROM technicien WHERE idTechnicien = ?"
    return cursor.execute(statement, [idTech]).fetchone()