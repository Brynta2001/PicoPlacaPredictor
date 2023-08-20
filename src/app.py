import sys

from src.predictor import Predictor
from src.validator import Validator

validator = Validator()
predictor = Predictor()


def run():
    while True:
        date = input("Enter a date in format dd/mm/yyyy\n")
        if not validator.validate_date_format(date):
            print("Invalid date")
            if int(input("Do you want to enter a date again? 0:Yes, 1:No\n")) != 0:
                sys.exit()
        else:
            break

    while True:
        time = input("Enter the time in 24H format hh:mm\n")
        if not validator.validate_time_format(time):
            print("Invalid time")
            if int(input("Do you want to enter a time again? 0:Yes, 1:No\n")) != 0:
                sys.exit()
        else:
            break

    while True:
        license_plate = input("Enter the license plate of the car like the example: PKD-0953\n")
        if not validator.validate_license_plate_format(license_plate):
            print("Invalid license plate")
            if int(input("Do you want to enter a license plate again? 0:Yes, 1:No\n")) != 0:
                sys.exit()
        else:
            break

    if predictor.predict(license_plate, date, time):
        print("The car can be on the road")
    else:
        print("The car can't be on the road")
