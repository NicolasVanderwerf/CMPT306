"""
Closest pair problem

This Tests the Closest Pair Program.

[Nicolas Van der Werf]
[August, 23, 2023]
"""

import unittest
import Closest
import sys

class MyTestCase(unittest.TestCase):
    def testClosest1(self):
        expected = (-13, -14)
        actual = Closest.closest_pair([-13, 5, 18, 7, -14, 21])
        print( "\nValues: [-13, 5, 18, 7, -14, 21]")
        print("Expected: (-13, -14)")
        self.assertEqual(expected, actual)  # add assertion here

    def testClosest2(self):
        expected = (-13, -13)
        actual = Closest.closest_pair([-13, 5, 18, 7, -14, 21, -13])
        print( "\nValues: [-13, 5, 18, 7, -14, 21, -13]")
        print("Expected: (-13, -13)")
        self.assertEqual(expected, actual)  # add assertion here



if __name__ == '__main__':
    unittest.main()
