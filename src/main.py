import sys

from src.predictor import Predictor
from src.validator import Validator

validator = Validator()
predictor = Predictor()

if __name__ == '__main__':
    date = input("Enter a date in format dd/mm/yyyy\n")
    if not validator.validate_date_format(date):
        print("Invalid date")
        sys.exit()

    time = input("Enter the time in 24H format hh:mm\n")
    if not validator.validate_time_format(time):
        print("Invalid time")
        sys.exit()

    license_plate = input("Enter the license plate of the car like the example: PKD-0953\n")
    if not validator.validate_license_plate_format(license_plate):
        print("Invalid license plate")
        sys.exit()

    if predictor.predict(license_plate, date, time):
        print("The car can be on the road")
    else:
        print("The car can't be on the road")