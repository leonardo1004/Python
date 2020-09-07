# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 21:08:46 2020

@author: Leonardo Quintero P
"""


import unittest
import ejericio3

class Testejercicio3(unittest.TestCase):
    def testcalcularnumero(self):
        self.assertEqual(ejercicio3.tomarpalabra("ximena"),("x","a"))
        
if __name__ == "__main__":
    unittest.main()