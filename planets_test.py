"""
@author Rookie
"""

from planets import *

def test_planets_positions():
    # setup
    periods = [1, 2, 4]
    semis = [0.33, 0.66, 1.00]
    time = 0.2

    expected_x = [
        math.cos(0.2) * 0.33,
        math.cos(0.1) * 0.66,
        math.cos(0.05) * 1.00
    ]
    expected_y = [
        math.sin(0.2) * 0.33,
        math.sin(0.1) * 0.66,
        math.sin(0.05) * 1.00
    ]

    # invoke
    actual_x, actual_y = planets_positions(periods, semis, time)

    # analyze
    assert expected_x == actual_x
    assert expected_y == actual_y