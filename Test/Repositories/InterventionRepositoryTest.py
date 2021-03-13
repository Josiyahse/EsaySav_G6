import unittest
from Repositories.interventionRepository import get_by_id
from Repositories.utils import get_cursor
from Repositories.interventionRepository import get_interventions
from Models.intervention import Intervention
from DataBase.manageDatabase import get_db
import json


class InterventionRepositoryTest (unittest.TestCase):
    def test_get_intervetion_by_id(self):
        get_inter = get_by_id(1);
        print(get_inter)
        self.assertEqual(get_inter['piece'],"Carte Graphique")

    def test_get_all_interventions(self):
        curseur = get_cursor()
        query = "SELECT * FROM intervention"
        interventions = curseur.execute(query).fetchall()
        self.assertEqual(interventions[0],{"idClient": 2,
            "idIntervention": 1,
            "idTechnicien": 1,
            "piece": "Carte Graphique",
            "probleme": "La carte graphique a cramé"
        })



if __name__ == '__main__':
    unittest.main()
