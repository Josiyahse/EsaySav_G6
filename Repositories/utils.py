from DataBase.manageDatabase import get_db


def to_dict(cursor, row):
    """
    :param cursor: curseur de la connexion
    :param row: toutes les lignes de la table qu'on veut par rapport à la requête du curseur
    :return: dictionnaire serializer de l'objet ou des objets dans la base des données avec comme format { key: value }
    """
    d = {}
    for idx, col in enumerate(cursor.description):
        """
            idx = index du nom du champ de la table (ex: Table Technicien: probleme->index n°3 comme ça commence à 0)
            col = nom du champ de la table (ex: Table Technicien: nom)
        """
        d[col[0]] = row[idx]
    return d


def get_cursor():
    db = get_db()
    db.row_factory = to_dict
    return db.cursor()
