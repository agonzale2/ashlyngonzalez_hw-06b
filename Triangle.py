
# -*- coding: utf-8 -*-
"""
Triangle Classification Program
@author: jrr
@author: rk
"""


def classifyTriangle(a, b, c):
    """
    Classifies three side lengths as Equilateral, Isoceles,
    Scalene, Right, NotATriangle, or InvalidInput.
    """

    # Validate input types
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # Check upper boundary
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # Check positive side lengths
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # Validate triangle inequality
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'

    # Classify equilateral triangles
    if a == b and b == c:
        return 'Equilateral'

    # Identify right triangles
    elif (a**2 + b**2 == c**2 or
          a**2 + c**2 == b**2 or
          b**2 + c**2 == a**2):
        return 'Right'

    # Classify scalene or isosceles triangles
    elif (a != b) and (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isoceles'







