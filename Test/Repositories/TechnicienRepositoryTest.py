import unittest
import sqlite3
from Repositories.technicienRepository import get_techniciens
from DataBase.manageDatabase import get_db
import json


class MyTestCase(unittest.TestCase):
    def test_something(self):
        cursor = sqlite3.connect("easySAV.db").cursor()
        query = f"SELECT * FROM technicien"
        reponse = cursor.execute(query)
        self.assertDictEqual(reponse[0],{
            "idTechnicien": 1,
            "nom": "Leclercq",
            "prenom": "Anthony"
        })


if __name__ == '__main__':
    unittest.main()
