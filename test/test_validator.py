import unittest

from src.validator import Validator


class TestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_validate_date_format(self):
        self.assertEqual(True, self.validator.validate_date_format("07/09/2001"))

    def test_validate_time_format(self):
        self.assertEqual(True, self.validator.validate_time_format("08:30"))

    def test_validate_license_plate_format(self):
        self.assertEqual(True, self.validator.validate_license_plate_format("PKD-0927"))
