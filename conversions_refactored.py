#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" refactors code from conversion.py to add in distance units, by Michael Hernandez  """

class ConversionNotPossible(Exception):
    """ Should be thrown if either a conversion unit is not found,
    or if there are no units to convert to/from
    """
    pass

def convert(src=str, dest=str, value=int):
    """ Converts units of measurements using a nested conversion dictionary """
    srcUnit = src.lower()
    destUnit = dest.lower()

    unitDict = {
        'kelvin': {'fahrenheit': (float(value) * 9/5) - 459.67, 'celsius': float(value) - 273.15},
        'celsius': {'fahrenheit': float(value) * 9/5 + 32, 'kelvin': float(value) + 273.15},
        'fahrenheit': {'celsius': (float(value) - 32) * 5/9,
                       'kelvin': (float(value) + 459.67) * 5/9},
        'miles': {'yards': value * 1760, 'meters': value * 1609.344},
        'yards': {'miles': float(value) / 1760, 'meters': float(value) / 1.094},
        'meters': {'miles': float(value) / 1609.344, 'yards': float(value) * 1.094}
    }

    if srcUnit == destUnit:
        answer = float(value)
        return round(answer, 2)
    else:
        try:
            answer = unitDict[srcUnit][destUnit]
            return round(answer, 2)
        except KeyError:
            raise ConversionNotPossible
