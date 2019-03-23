import unittest
import conversions
import conversions_refactored
""" Test conversions unittest package """

class TestConversions(unittest.TestCase):
    """ A class to test out the conversion module - I'm using a dictionary to create the test cases """
    testCases = [
        {"celsius": 200.00, "fahrenheit": 392.00, "kelvin": 473.15},
        {"celsius": 125.00, "fahrenheit": 257.00, "kelvin": 398.15},
        {"celsius": 0.00, "fahrenheit": 32.00, "kelvin": 273.15},
        {"celsius": 232.78, "fahrenheit": 451.00, "kelvin": 505.93},
        {"celsius": -231.15, "fahrenheit": -384.07, "kelvin": 42}
    ]

    def testCelciusToKelvin(self):
        """ Test from Celsius to Kelvin """
        for test in self.testCases:
            result = conversions.convertCelsiusToKelvin(test["celsius"])
            self.assertEqual(test["kelvin"], result)

    def testCelsiusToFahrenheit(self):
        for test in self.testCases:
            result = conversions.convertCelsiusToFahrenheit(test["celsius"])
            self.assertEqual(test["fahrenheit"], result)

    def testFahrenheitToCelsius(self):
        for test in self.testCases:
            result = conversions.convertFahrenheitToCelsius(test["fahrenheit"])
            self.assertEqual(test["celsius"], result)

    def testFahrenheitToKelvin(self):
        for test in self.testCases:
            result = conversions.convertFahrenheitToKelvin(test["fahrenheit"])
            self.assertEqual(test["kelvin"], result)

    def testKelvinToFahrenheit(self):
        for test in self.testCases:
            result = conversions.convertKelvinToFahrenheit(test["kelvin"])
            self.assertEqual(test["fahrenheit"], result)

    def testKelvinToCelsius(self):
        for test in self.testCases:
            result = conversions.convertKelvinToCelsius(test["kelvin"])
            self.assertEqual(test["celsius"], result)

class testConvert(unittest.TestCase):
    """This class defines the test  for the convert function in
    conversions_refactored.py."""


    def testConvertTempurature(self):
        """convert() should give known temperature result with known input."""
        self.assertEqual(conversions_refactored.convert(
            'celsius', 'kelvin', 200), 473.15)
        self.assertEqual(conversions_refactored.convert(
            'celsius', 'fahrenheit', 125), 257.00)
        self.assertEqual(conversions_refactored.convert(
            'fahrenheit', 'celsius', 32), 0.00)
        self.assertEqual(conversions_refactored.convert(
            'fahrenheit', 'kelvin', 451), 505.93)
        self.assertEqual(conversions_refactored.convert(
            'kelvin', 'fahrenheit', 42), -384.07)
        self.assertEqual(conversions_refactored.convert(
            'kelvin', 'celsius', 200), -73.15)

    def testMirrorTemperature(self):
        self.assertEqual(conversions_refactored.convert(
            'celsius', 'celsius', 300), 300.00)
        self.assertEqual(conversions_refactored.convert(
            'fahrenheit', 'fahrenheit', 35), 35.00)
        self.assertEqual(conversions_refactored.convert(
            'kelvin', 'kelvin', 272), 272.00)


if __name__ == '__main__':
    unittest.main()
