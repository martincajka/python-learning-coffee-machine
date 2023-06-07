from enum import Enum


class States(Enum):
    choosing_an_action = 1
    choosing_coffee = 2
    taking_cash = 3
    filling_machine = 4
    checking_supplies = 5
    exit = 6
