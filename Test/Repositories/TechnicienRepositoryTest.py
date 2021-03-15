import unittest
from main.Repositories.utils import get_cursor
from main.Repositories.technicienRepository import get_by_id


class MyTestCase(unittest.TestCase):
    def test_get_techniciens(self):

        dico_technicien = {
            "idTechnicien": 1,
            "nom": "Leclercq",
            "prenom": "Anthony"
        }

        curseur = get_cursor()
        query = f"SELECT * FROM technicien"
        reponse = curseur.execute(query).fetchall()
        self.assertEqual(reponse[0],dico_technicien)


    def test_get_technicien_by_id(self):
        get_techniciens = get_by_id(3)
        self.assertEqual(get_techniciens['nom'],'Lecomte')

if __name__ == '__main__':
    unittest.main()
