""" Test conversions unittest package, by Michael Hernandez  """
import unittest
import random
import conversions
import conversions_refactored


class TestConversions(unittest.TestCase):
    """ A class to test out the conversion module - I'm using a dictionary to
    create the test cases """
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
        """ Test from Celsius to Fahrenheit """
        for test in self.testCases:
            result = conversions.convertCelsiusToFahrenheit(test["celsius"])
            self.assertEqual(test["fahrenheit"], result)

    def testFahrenheitToCelsius(self):
        """ Test from Celsius to Kelvin """
        for test in self.testCases:
            result = conversions.convertFahrenheitToCelsius(test["fahrenheit"])
            self.assertEqual(test["celsius"], result)

    def testFahrenheitToKelvin(self):
        """ Test from Celsius to Kelvin """
        for test in self.testCases:
            result = conversions.convertFahrenheitToKelvin(test["fahrenheit"])
            self.assertEqual(test["kelvin"], result)

    def testKelvinToFahrenheit(self):
        """ Test from Celsius to Kelvin """
        for test in self.testCases:
            result = conversions.convertKelvinToFahrenheit(test["kelvin"])
            self.assertEqual(test["fahrenheit"], result)

    def testKelvinToCelsius(self):
        """ Test from Celsius to Kelvin """
        for test in self.testCases:
            result = conversions.convertKelvinToCelsius(test["kelvin"])
            self.assertEqual(test["celsius"], result)

class TestConversionRefactored(unittest.TestCase):
    """ Testing the refactored code using random test cases """
    randomSet = random.sample(range(-50, 4000), 8)

    def testConvertTempurature(self):
        """ Our refactored function should calculate all conversions correctly
        according to the formulas provided."""
        for test in self.randomSet:

            celsiusToKelvin = round(float(test) + 273.15, 2)
            celsiusToFahrenheit = round(float(test) * 9 / 5 + 32, 2)
            fahrenheitToCelsius = round((float(test) - 32) * 5 / 9, 2)
            fahrenheitToKelvin = round((float(test) + 459.67) * 5 / 9, 2)
            kelvinToFahrenheit = round(float(test) * 9 / 5 - 459.67, 2)
            kelvinToCelsius = round(float(test) - 273.15, 2)
            yardsToMiles = round(float(test) / 1760, 2)
            yardsToMeters = round(float(test) / 1.094, 2)
            metersToYards = round(float(test) * 1.094, 2)
            metersToMiles = round(float(test) / 1609.344, 2)
            milesToYards = round(float(test) * 1760, 2)
            milesToMeters = round(float(test) * 1609.344, 2)

            self.assertEqual(conversions_refactored.convert(
                'celsius', 'kelvin', test), celsiusToKelvin)
            self.assertEqual(conversions_refactored.convert(
                'celsius', 'fahrenheit', test), celsiusToFahrenheit)
            self.assertEqual(conversions_refactored.convert(
                'fahrenheit', 'celsius', test), fahrenheitToCelsius)
            self.assertEqual(conversions_refactored.convert(
                'fahrenheit', 'kelvin', test), fahrenheitToKelvin)
            self.assertEqual(conversions_refactored.convert(
                'kelvin', 'fahrenheit', test), kelvinToFahrenheit)
            self.assertEqual(conversions_refactored.convert(
                'kelvin', 'celsius', test), kelvinToCelsius)
            self.assertEqual(conversions_refactored.convert(
                'yards', 'miles', test), yardsToMiles)
            self.assertEqual(conversions_refactored.convert(
                'yards', 'meters', test), yardsToMeters)
            self.assertEqual(conversions_refactored.convert(
                'meters', 'yards', test), metersToYards)
            self.assertEqual(conversions_refactored.convert(
                'meters', 'miles', test), metersToMiles)
            self.assertEqual(conversions_refactored.convert(
                'miles', 'yards', test), milesToYards)
            self.assertEqual(conversions_refactored.convert(
                'miles', 'meters', test), milesToMeters)



    def testIdentityCase(self):
        """ Tests to see if the conversions_refactored module returns the same result if the
        source and destination units are the same"""
        testSet = ['fahrenheit', 'celsius', 'kelvin', 'miles', 'meters', 'yards']

        for item in testSet:
            unit1 = unit2 = item
            for value in self.randomSet:
                self.assertEqual(conversions_refactored.convert(unit1, unit2, value), int(value))


    def testFailedCases(self):
        """ Tests to see if the conversions_refactored module throws a ConversionNotPossible
        exception error if we try to convert units either not found in the dictionary,
        or that cannot be converted """
        failedTestSet = {'celsius': 'miles', 'fahrenheit': 'mile', 'miles':'inches'}

        for src, dest in failedTestSet.items():
            self.assertRaises(conversions_refactored.ConversionNotPossible,
                              conversions_refactored.convert, src, dest, 200)

if __name__ == '__main__':
    unittest.main()
