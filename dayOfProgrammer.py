
def dayOfProgrammer(year):
    programmer_day = ''
    if year == 1918:
        programmer_day = '26.09.1918'
    elif year < 1919:
        programmer_day = calculate_by_julian(year)
    else:
        programmer_day = calculate_by_gregorian(year)
    return programmer_day

def calculate_by_gregorian(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return f'12.09.{year}'
    else:
        return f'13.09.{year}'

def calculate_by_julian(year):
    if year % 4 == 0:
        return f'12.09.{year}'
    else:
        return f'13.09.{year}'
