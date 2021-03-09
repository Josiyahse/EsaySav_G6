from DataBase.manageDatabase import get_db


def to_dict(cursor, row):
    """

    """
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_cursor():
    db = get_db()
    db.row_factory = to_dict
    return db.cursor()
