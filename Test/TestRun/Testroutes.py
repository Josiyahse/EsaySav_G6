import unittest
from run import app,get_interventions,get_intervention_by_id
import json


class TestRoutes(unittest.TestCase):

    def test_route_get_all(self):
        with app.app_context():
            client = app.test_client()
            url = '/interventions'

            response = client.get(url)
            assert response.status_code == 200

    def test_get_by_id(self):
        with app.app_context():
            client = app.test_client()
            url = '/intervention/1'

            response = client.get(url)
            assert response.status_code == 200

    def test_add_intervention(self):
        with app.app_context():
            client = app.test_client()
            url = '/intervention/add'

            response = client.get(url)
            assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()
