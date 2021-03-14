import unittest
from run import app
import Repositories.technicienRepository as technicienController
import json


class TestRoutes(unittest.TestCase):
    def Test_app(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.app = app.test_client()
        self.assertEqual(app.debug, True)

    def test_route_get_all(self):
        response = self.app.get('/interventions')
        self.assertEqual(response.status_code, 200)

    def test_route_intervention_save(self):
        response = self.app.post('/add', content_type='application/json', data=json.dumps({}))
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
