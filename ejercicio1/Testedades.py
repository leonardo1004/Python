import unittest
import edades

class Testedades(unittest.TestCase):

	def testcalcular_edad(self):
        	self.assertEqual(edades.calcular_edad(18, 2020), 68)
        
if __name__ == "__main__":
    unittest.main()