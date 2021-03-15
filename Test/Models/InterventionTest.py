import unittest
from main.Models.intervention import Intervention

class InterventionTest (unittest.TestCase):
    def test_create_intervention(self):
        intervention = Intervention(54,48,'Ordinateur','le processeur')
        self.assertIsNotNone(intervention)

if __name__ == '__main__':
    unittest.main()
