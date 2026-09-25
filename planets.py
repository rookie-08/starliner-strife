"""
Writes a .csv file about the scores of different planet colonies
over time.

@author Rookie
""" # About


"""
Planet Lists: constant_period, constant_axis, theta, x, y, closest, score

Final Lists: A 2D list, each row is the format for the output file

Main: A large for loop that does the following:

    - Move the planets

    - Calculate the distances and thus the closest

    - Make informed decisions (score add)

    - (score decay)

Main 2: Write the file.

Output file: days passed, score0, score1, score 2, ...

""" # How this script works


"""
General Development

- Implement each of the functions

""" # Tasks

import math

# Static configuarion variables
PLANETS_PERIODS = []
PLANETS_SEMIS = []
"""A non-jagged 2D list. Each row stores the time of the simulation, then the scores of each planet."""

def planets_positions(periods, semis, time):
    """
    Calculates the position of the planets using the updated `time`,
    as well as the list of the planets' `periods` (orbital periods)
    and `semis` (orbital semi-major axes).
    
    Returns two variables: the list of the planets' x-coordinates,
    and the list of the planets' y-coordinates.
    """

    """
    "p" denotes the individual planet being analyzed
    `i` denotes the index of "p"
    `s` denotes the semi-major-axis of "p"
    `t` denotes the period of "p"
    `a` denotes the angle/theta of "p"
    `x` denotes the x-coordinate of "p"
    `y` denotes the y-coordinate of "p"

    """

    # initialize
    planets_x = []
    planets_y = []

    # loop over list of periods
    length_of_planets_list = len(periods)
    for i in range(length_of_planets_list):
        # given
        t = periods[i]
        s = semis[i]
        # calculate
        a = time / t
        x = s * math.cos(a)
        y = s * math.sin(a)
        # append
        planets_x.append(x)
        planets_y.append(y)

    # return two lists at once
    return planets_x, planets_y

def distance_basic(x1, y1, x2, y2):
    """
    Returns the distance between the two points (`x1`, `y1`) and (`x2`, `y2`).
    """

    dx = (x1 - x2)
    dy = (y1 - y2)

    return math.sqrt(dx * dx + dy * dy)

def planet_distance(planets_x, planets_y, i, j):
    """
    Returns the distance between planet `i` and planet `j`,
    given the two lists of planetary coordinates `planets_x`
    and `planets_y`.
    """

    x1 = planets_x[i]
    y1 = planets_y[i]
    x2 = planets_x[j]
    y2 = planets_y[j]

    return distance_basic(x1, y1, x2, y2)

def planet_closest_destination(planets_x, planets_y, i):
    """
    Returns the index of the closest destination planet to planet
    `i`, given the two lists of planetary coordinates `planets_x`
    and `planets_y`.
    """

    # Variable distance_is_set
    # Variable min_distance
    # Variable held_index_j

    # For j = 0, 7
        # Get distance from i to j using `planet_distance()`
        # j == i?
            # ignore
        # elif: distance not is set?
            # automatically set and ignore
        # else (compare)
            # current distance is less than stored distance?
                # set new distance and held j
            # else

    # return j

    distance_is_set = False
    min_distance = 0
    held_index_j = -1

    length_of_list = len(planets_x)
    for j in range(length_of_list):
        dist_i_j = planet_distance(planets_x, planets_y, i, j)
        if (i == j):
            ...
        elif (not distance_is_set):
            distance_is_set = True
            min_distance = dist_i_j
            held_index_j = j
        else:
            if (dist_i_j < min_distance):
                min_distance = dist_i_j
                held_index_j = j

    return held_index_j

def planets_closests(planets_x, planets_y):
    """
    Returns a list of the closest destinations to each planet, given
    the 2 lists of coordinates `planets_x` and `planets_y`.
    """

    # Initialize
    planets_closest = []
    # Loop
    for i in range(len(planets_x)):
        # Get closest destination to i
        j = planet_closest_destination(planets_x, planets_y, i)
        # Add destination index to list
        planets_closest.append(j)
    # Return
    return planets_closest

def planets_adds(planets_scores, planets_closest):
    """
    Adds +1 to an element in `planets_scores` each time its
    index is found in `planets_closest`.
    
    Returns the modified `planets_scores` list. 
    """

    for i in planets_closest:
        planets_scores[i] = planets_scores[i] + 1.0

    return planets_scores

def planets_decays(planets_scores):
    """
    Multiplies every element in `planets_scores` by 0.9.

    Returns the modified `planets_scores`.
    """

    for i in range(len(planets_scores)):
        planets_scores[i] = planets_scores[i] * 0.9 # Potentially softcodable
    return planets_scores

def add_to_dataset(planet_dataset, planets_scores, time):
    """
    Copies `planets_scores`, inserts `time` at the first index of
    the copy, then appends the modified copy to `planet_dataset`.
    
    Returns the modified `planet_dataset`.

    The copy, added to `planet_dataset`, looks like this:
    `[time, planets_scores[0], planets_scores[1], ..., planets_scores[7]]`
    """

    planet_dataset.append([time] + planets_scores)
    return planet_dataset

def simulate(length, p_periods, p_semis):
    """
    Runs a simulation of `length` days long and adds the collected data to a dataset.

    When going through each iteration, it moves the planets, then scores the planets.

    Returns the resultant dataset that represents the scores appearing throughout the
    simulation.
    """

    planets_x = []
    planets_y = []
    planets_dests = []
    planets_scores = [0.0 for _ in range(len(p_periods))]
    p_dataset = []

    for time in range(0, length, 10):
        planets_x, planets_y = planets_positions(p_periods, p_semis, time)
        planets_dests = planets_closests(planets_x, planets_y)
        planets_scores = planets_adds(planets_scores, planets_dests)
        planets_scores = planets_decays(planets_scores)
        p_dataset = add_to_dataset(p_dataset, planets_scores, time)

    return p_dataset

def write_dataset(dataset, path):
    """
    Stores `dataset` as a .csv file in `path`.
    """

    a_string = ""

    for row in dataset:
        element_string = ""
        for element in row:
            element_string = element_string + str(element) + ","
        element_string = element_string[0:-1]
        a_string = a_string + element_string + "\n"
    a_string = a_string[0:-1]

    with open(path, "w") as file:
        file.write(a_string)

def main():
    """
    Writes a dataset representing a simulation that it runs over
    the course of multiple simulated days.
    """
    
    planets_dataset = simulate(1000, PLANETS_PERIODS, PLANETS_SEMIS)
    print(planets_dataset)
    write_dataset(planets_dataset, "scores.csv")

if (__name__ == "__main__"):
    main()