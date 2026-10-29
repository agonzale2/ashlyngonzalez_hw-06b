
# -*- coding: utf-8 -*-
"""
M07.A07b - Testing a Legacy System
Unit tests for the classifyTriangle() function.
"""

import unittest
from Triangle import classifyTriangle


class TestTriangles(unittest.TestCase):

    def check_triangles(self, cases):
        """Test multiple inputs against their expected results."""
        for sides, expected in cases:
            with self.subTest(sides=sides):
                self.assertEqual(classifyTriangle(*sides), expected)

    def testRightTriangles(self):
        self.check_triangles([
            ((3, 4, 5), 'Right'),
            ((5, 3, 4), 'Right'),
            ((4, 5, 3), 'Right'),
            ((60, 80, 100), 'Right')
        ])

    def testEquilateralTriangles(self):
        self.check_triangles([
            ((1, 1, 1), 'Equilateral'),
            ((50, 50, 50), 'Equilateral'),
            ((200, 200, 200), 'Equilateral')
        ])

    def testIsoscelesTriangles(self):
        self.check_triangles([
            ((5, 5, 8), 'Isoceles'),
            ((5, 8, 5), 'Isoceles'),
            ((8, 5, 5), 'Isoceles')
        ])

    def testScaleneTriangles(self):
        self.check_triangles([
            ((4, 5, 6), 'Scalene'),
            ((6, 4, 5), 'Scalene'),
            ((5, 6, 4), 'Scalene')
        ])

    def testNotATriangle(self):
        self.check_triangles([
            ((1, 2, 3), 'NotATriangle'),
            ((3, 1, 2), 'NotATriangle'),
            ((2, 3, 1), 'NotATriangle'),
            ((2, 3, 10), 'NotATriangle')
        ])

    def testInvalidInputs(self):
        self.check_triangles([
            ((0, 4, 5), 'InvalidInput'),
            ((4, 0, 5), 'InvalidInput'),
            ((4, 5, 0), 'InvalidInput'),
            ((-1, 4, 5), 'InvalidInput'),
            ((4, -1, 5), 'InvalidInput'),
            ((4, 5, -1), 'InvalidInput'),
            ((201, 100, 100), 'InvalidInput'),
            ((100, 201, 100), 'InvalidInput'),
            ((100, 100, 201), 'InvalidInput')
        ])

    def testNonIntegerInputs(self):
        self.check_triangles([
            ((3.5, 4, 5), 'InvalidInput'),
            (("3", 4, 5), 'InvalidInput'),
            ((None, 4, 5), 'InvalidInput')
        ])


if __name__ == '__main__':
    unittest.main()



