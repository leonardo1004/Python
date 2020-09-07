# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 20:27:58 2020

@author: Leonardo Quintero P
"""


import unittest
import ejericio2

class Testejercicio2(unittest.TestCase):
    def testcalcularnumero(self):
        self.assertEqual(ejercicio2.calcular(90), True)
        self.assertEqual(ejercicio2.calcular(153), False)
        
if __name__ == "__main__":
    unittest.main()
        