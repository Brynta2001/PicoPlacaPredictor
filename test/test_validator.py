import unittest

from src.validator import Validator


class TestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_validate_date_format(self):
        self.assertEqual(True, self.validator.validate_date_format("07/09/2001") )
