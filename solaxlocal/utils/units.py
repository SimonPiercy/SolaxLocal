class Unit:
    pass


MAX_16_BIT = 2 ** 16
MAX_SIGNED_16_BIT = 2 ** 15 - 1


def signed_16_bit(value: int) -> int:
    return value if value < MAX_SIGNED_16_BIT else value - MAX_16_BIT


def dual_register(value1: int, value2) -> int:
    return value1 + value2 * MAX_16_BIT


class Hz(float):
    unit_of_measure = 'Hz'


class Volts(float):
    unit_of_measure = 'Volts'


class Amps(float):
    unit_of_measure = 'Amps'


class Watts(float):
    unit_of_measure = 'Watts'


class Kwh(float):
    unit_of_measure = 'kWh'


class Percent(float):
    unit_of_measure = '%'


class DegreesC(float):
    unit_of_measure = '°C'
