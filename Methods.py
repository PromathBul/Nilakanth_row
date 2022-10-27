def enter (message):
    num = int(input(message))
    return num

def calculate_pi (accuracy):
    d = 10 ** -accuracy
    pi = 3
    significant = 4
    value = 1
    while d < abs(value):
        value = 4 / significant / (significant - 1) / (significant - 2)
        if significant % 4 != 0:
            value *= -1
        pi += value
        significant += 2
    return int(pi * 10 ** accuracy) / 10 ** accuracy