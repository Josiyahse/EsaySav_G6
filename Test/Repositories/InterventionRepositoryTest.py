import unittest
from Repositories.interventionRepository import get_by_id
from Repositories.interventionRepository import get_interventions
from Models.intervention import Intervention
from DataBase.manageDatabase import get_db
import json


class InterventionRepositoryTest (unittest.TestCase):
    def test_get_intervetion(self):
        get_inter = get_by_id(1);
        self.assertEqual(get_inter.piece,"Carte Graphique")

    def test_get_all_interventions(self):
        cursor = get_db().cursor()
        query = "SELECT * FROM intervention"
        interventions = cursor.execute(query)
        self.assertDictEqual(interventions[0],{"idClient": 2,
            "idIntervention": 1,
            "idTechnicien": 1,
            "piece": "Carte Graphique",
            "probleme": "La carte graphique a cramé"
        })



if __name__ == '__main__':
    unittest.main()
