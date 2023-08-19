import unittest
from src.predictor import Predictor

class TestPredictor(unittest.TestCase):
    def setUp(self):
        self.predictor = Predictor()

    def test_return_last_digit_of_license_plate(self):
        self.assertEqual(7, self.predictor.return_last_digit("PKD-0927"))