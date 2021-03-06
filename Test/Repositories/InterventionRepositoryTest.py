import unittest
from main.Repositories.interventionRepository import get_by_id
from main.Repositories.utils import get_cursor
from main.Repositories.interventionRepository import add_intervention
from main.Models.intervention import Intervention


class InterventionRepositoryTest (unittest.TestCase):
    def test_get_intervetion_by_id(self):
        get_inter = get_by_id(1)
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

    def test_insert_intervetion(self):
        intervention = Intervention(54, 48, 'Ordinateur', 'le processeur')
        test_insert = add_intervention(intervention)
        print(test_insert)
        self.assertEqual(test_insert, 1)


if __name__ == '__main__':
    unittest.main()
