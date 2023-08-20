# Pico&Placa Predictor
This application allows you to determine whether or not a vehicle can circulate on the streets according to the Pico&Placa restriction in Quito. The code was generated in python using PyCharm IDE and can be executed through a console. For the entry, the license plate of the car, the date and time are received, and a message is returned indicating whether the vehicle can circulate or not.
This program considers the holidays of the year 2023; however, it is possible to modify the code to take into account later years.
Also, it is important to consider that the program uses the past Pico&Placa rules, which are:
- Restricted hours in the morning: 7:00 - 9:30.
- Restricted hours in the morning: 16:00 - 19:30.
- Cars with license plates ending in 1 and 2 cannot circulate on Monday.
- Cars with license plates ending in 3 and 4 cannot circulate on Tuesday.
- Cars with license plates ending in 5 and 6 cannot circulate on Wednesday.
- Cars with license plates ending in 7 and 8 cannot circulate on Thursday.
- Cars with license plates ending in 9 and 0 cannot circulate on Friday.
- Cars can circulate freely on holidays and weekends.


## Installation

The program does not require additional dependencies. To use it, it is only necessary to execute the "main.py" file.


## Usage

1. Execute the "main.py" file using a console or a python IDE.
2. The console will ask you to enter the license plate, date and time separately.
3. Enter the date in this format: dd/mm/yyyy.
4. Enter the time using 24H format: hh:mm.
5. Enter the license plate like this: AAA-0999.
6. The console will display a message indicating whether the vehicle can circulate on the street or not.

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


## Test

The code includes unit tests inside of the "tests" directory. You can run them with unittest library.
Here you have some important cases that you could use to test the "predictor" method, or even the whole program.

| License Plate |    Date    |  Time |  Can road |            Message           |
| ------------- | ---------- | ----- | --------- | ---------------------------- |
|   PKD-0927    | 20/08/2023 | 20:50 |   True    | The car can be on the road   |
|   PKD-0921    | 07/08/2023 | 16:30 |   False   | The car can't be on the road |
|   ABD-0921    | 02/01/2023 | 07:50 |   True    | The car can be on the road   |
|   CDA-1429    | 18/08/2023 | 08:30 |   False   | The car can't be on the road |
|   CDA-1429    | 18/08/2023 | 12:30 |   True    | The car can be on the road   |

## Observations
The project works on PyCharm; however, if you want to clone the repository and use it with Visual Studio Code there may be a problem with the packages, but it is only necessary to remove "src" in the "imports".


## License

Copyright (c) 2023 Bryan Tapia.
This project is [MIT](https://github.com/Brynta2001/PicoPlacaPredictor/blob/master/LICENSE) licensed.
