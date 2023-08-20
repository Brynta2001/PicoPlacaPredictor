import unittest
from datetime import date, time

from src.predictor import Predictor


class TestPredictor(unittest.TestCase):
    def setUp(self):
        self.predictor = Predictor()

    def test_return_last_digit_of_license_plate(self):
        self.assertEqual(7, self.predictor.return_last_digit("PKD-0927"))

    def test_is_holiday(self):
        self.assertEqual(True, self.predictor.is_holiday(date(2023, 1, 2)))

    def test_is_in_time_range(self):
        self.assertEqual(True, self.predictor.is_in_time_range(time(12, 30)))

    def test_predict_if_pico_and_placa_applies(self):
        self.assertEqual(True,
                         self.predictor.predict("PKD-0921", "02/02/2023", "08:30"))
