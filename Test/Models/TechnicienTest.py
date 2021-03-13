import unittest
from Models.technicien import Technicien

class TestTechnicien(unittest.TestCase):
    def test_something(self):
        technicien = Technicien('Menvu','Gerard')
        self.assertIsNotNone(technicien)


if __name__ == '__main__':
    unittest.main()
