import conversions
import unittest

class TestConversions(unittest.TestCase):

	testCases = [
		{"C": 300.00, "F": 572.00, "K": 573.15},
		{"C": 300.00, "F": 572.00, "K": 573.15},
		{"C": 300.00, "F": 572.00, "K": 573.15},
		{"C": 300.00, "F": 572.00, "K": 573.15},
		{"C": 300.00, "F": 572.00, "K": 573.15}
	]

	def testCelciusToKelvin(self):
		for test in self.testCases:
			result = conversions.convertCelsiustoKelvin(test["C"])
			self.assertEqual(test["K"], result)

	def testCelciusToFahrenheit(self):
		for test in self.testCases:
			result = conversions.convertCelsiustoKelvin(test["C"])
			self.assertEqual(test["F"], result)

	def testFahrenheitToCelcius(self):
		for test in self.testCases:
			result = conversions.convertCelsiustoKelvin(test["F"])
			self.assertEqual(test["C"], result)

	def testFahrenheitToKelvin(self):
		for test in self.testCases:
			result = conversions.convertCelsiustoKelvin(test["F"])
			self.assertEqual(test["K"], result)

	def testKelvinToFahrenheit(self):
		for test in self.testCases:
			result = conversions.convertCelsiustoKelvin(test["K"])
			self.assertEqual(test["F"], result)

	def testKelvinToCelsius(self):
		for test in self.testCases:
			result = conversions.convertCelsiustoKelvin(test["K"])
			self.assertEqual(test["C"], result)


class testConvert(unittest.TestCase):
    """This class defines the test  for the convert function in
    conversions_refactored.py."""


    def testConvertTempurature(self):
        """convert() should give known temperature result with known input."""
        self.assertEqual(conversions_refactored.convert(
            'celsius', 'kelvin', 300), 573.15)
        self.assertEqual(conversions_refactored.convert(
            'celsius', 'fahrenheit', 390), 734.00)
        self.assertEqual(conversions_refactored.convert(
            'fahrenheit', 'celsius', -238), -150.00)
        self.assertEqual(conversions_refactored.convert(
            'fahrenheit', 'kelvin', 734), 663.15)
        self.assertEqual(conversions_refactored.convert(
            'kelvin', 'fahrenheit', 0), -459.67)
        self.assertEqual(conversions_refactored.convert(
            'kelvin', 'celsius', 413.15), 140.00)