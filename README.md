# Pico&Placa Predictor
This application allows you to determine whether or not a vehicle can circulate on the streets according to the Pico&Placa restriction in Quito. The code is generated in python and can be used through a console. For the entry, the license plate of the car, the date and time are received, and a message is returned indicating whether the vehicle can circulate or not.
This program considers the holidays of the year 2023; however, it is possible to modify the code to take into account later years.


## Installation

The program does not require additional dependencies. To use it, it is only necessary to execute the "main.py" file.


## Usage

1. Execute the "main.py" file using a console or a python IDE.
2. The console will ask you to enter the license plate, date and time separately.
3. Enter the license plate, date and time with the specified formats.
4. The console will display a message indicating whether the vehicle can circulate on the street or not.

## Modify the program to include holidays

The code works considering the holidays of the year 2023. 
If you want to include holidays of later years you can add them by changing the class "Holiday" inside the "schedule.py" file.
```python
class Holiday(Enum):
    NEW_YEAR = date(2023, 1, 2)
    CARNAVAL_1 = date(2023, 2, 20)
    CARNAVAL_2 = date(2023, 2, 21)
    GOOD_FRIDAY = date(2023, 4, 7)
    LABOR_DAY = date(2023, 5, 1)
    PICHINCHA_BATTLE = date(2023, 5, 26)
    FIRST_CRY_OF_INDEPENDENCE = date(2023, 8, 11)
    GUAYAQUIL_INDEPENDENCE = date(2023, 10, 9)
    DAY_OF_THE_DEAD = date(2023, 11, 2)
    CUENCA_INDEPENDENCE = date(2023, 11, 3)
    QUITO_FOUNDATION = date(2023, 12, 4)
    CHRISTMAS = date(2023, 12, 25)
```


## License

Copyright (c) 2023 Bryan Tapia
This project is [MIT](https://github.com/Brynta2001/PicoPlacaPredictor/blob/master/LICENSE) licensed.
