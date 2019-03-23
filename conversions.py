#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Unit conversion functions, by Michael Hernandez """

def convertCelsiusToKelvin(celcius):
    """ function to convert Celsius to Kelvin """
    kelvin = float(celcius) + 273.15
    return round(kelvin, 2)

def convertCelsiusToFahrenheit(celcius):
    """ function to convert Celsius to Fahrenheit """
    fahrenheit = (float(celcius) * 1.8) + 32
    return round(fahrenheit, 2)

def convertFahrenheitToCelsius(fahrenheit):
    """ function to convert Fahrenheit to Celsius """
    celcius = (float(fahrenheit) -32) * 5 / 9
    return round(celcius, 2)

def convertFahrenheitToKelvin(fahrenheit):
    """ function to convert Fahrenheit to Kelvin """
    kelvin = (float(fahrenheit) + 459.67) * 5/9
    return round(kelvin, 2)

def convertKelvinToFahrenheit(kelvin):
    """ function to convert Kelvin to Fahrenheit """
    fahrenheit = float(kelvin) * 9/5 - 459.67
    return round(fahrenheit, 2)

def convertKelvinToCelsius(kelvin):
    """ function to convert Kelvin to Celsius """
    celcius = kelvin - 273.15
    return round(celcius, 2)
