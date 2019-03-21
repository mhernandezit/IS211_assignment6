from __future__ import division

def convertCelsiusToKelvin(celcius):
    kelvin = float(celcius) + 273.15
    return round(kelvin, 2)

def convertCelsiusToFahrenheit(celcius):
    fahrenheit = (float(celcius) * 1.8) + 32
    return round(fahrenheit, 2)

def convertFahrenheitToCelsius(fahrenheit):
    celcius = (float(fahrenheit) -32) * 5 / 9
    return round(celcius, 2)

def convertFahrenheitToKelvin(fahrenheit):
    kelvin = (float(fahrenheit) + 459.67) * 5/9
    return round(kelvin, 2)

def convertKelvinToFahrenheit(kelvin):
    fahrenheit = float(kelvin) * 9/5 - 459.67
    return round(fahrenheit, 2)

def convertKelvinToCelsius(kelvin):
    celcius = kelvin - 273.15
    return round(celcius, 2)
