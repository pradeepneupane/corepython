#temperature.py
"""convert the temperature"""

#functions
def to_celcius(x):
    """"temp convert into celcius"""
    return 5*(x-32)/9.0

def to_fahren(x):
    """"temp convert into fahrenheit"""
    return 9*x/5.0+32

#constants
FREEZING_C = 0.0
FREEZING_F = 32.0