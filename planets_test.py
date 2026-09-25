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

def test_distance_basic():
    # setup
    x1 = 3.0
    y1 = 5.0
    x2 = 7.0
    y2 = 2.0
    expected = 5.0

    # invoke
    actual = distance_basic(x1, y1, x2, y2)

    # analyze
    assert expected == actual

def test_planet_distances():
    # setup
    planets_x = [-1.0, 6.0, 8.0]
    planets_y = [1.0, -3.0, -2.0]
    i = 0
    j = 1
    expected = math.sqrt(65.0)

    # invoke
    actual = planet_distance(planets_x, planets_y, i, j)

    # analyze
    assert expected == actual

def test_planet_closest_destination():
    # setup
    planets_x = [-1.0, 6.0, 8.0]
    planets_y = [1.0, -3.0, -2.0]
    i = 1
    expected = 2

    # invoke
    actual = planet_closest_destination(planets_x, planets_y, i)

    # analyze
    assert expected == actual

def test_planets_closests():
    # setup
    planets_x = [-1.0, 6.0, 8.0]
    planets_y = [1.0, -3.0, -2.0]
    expected = [1, 2, 1]

    # invoke
    actual = planets_closests(planets_x, planets_y)

    # analyze
    assert expected == actual

def test_planets_adds():
    # setup
    planets_scores = [2.0, 5.0, 7.0, 9.0]
    planets_closest = [1, 1, 2, 0]
    expected = [3.0, 7.0, 8.0, 9.0]

    # invoke
    actual = planets_adds(planets_scores, planets_closest)

    # analyze
    assert expected == actual

def test_planets_decays():
    # setup
    planets_scores = [2.0, 5.0, 7.0, 9.0]
    expected = [1.8, 4.5, 6.3, 8.1]

    # invoke
    actual = planets_decays(planets_scores)

    # analyze
    assert expected == actual

def test_add_to_dataset():
    # setup
    planet_dataset = [
        [],
        [],
        [],
        [],
        []
    ]
    planets_scores = [2.0, 3.0, 4.0]
    time = 60

    # invoke
    actual = add_to_dataset(planet_dataset, planets_scores, time)

    # analyze
    assert len(actual) == 6
    assert actual[5] == [60, 2.0, 3.0, 4.0]

def test_simulate():
    # setup
    length = 1000
    p_periods = [1, 2, 4]
    p_semis = [0.33, 0.66, 1.00]
    
    # invoke
    actual = simulate(length, p_periods, p_semis)

    # analyze
    assert len(actual) > 0