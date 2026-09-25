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
    ...

def planets_closests(planets_x, planets_y):
    """
    Returns a list of the closest destinations to each planet, given
    the 2 lists of coordinates `planets_x` and `planets_y`.
    """

    # new planets_closest list

    # for i = 0, 7
        # get the closest planet j using `planet_closest_destination()`
        # place j in index i of planets_closest

    # return planets_closest
    ...

def planets_adds(planets_scores, planets_closest):
    """
    Adds +1 to an element in `planets_scores` each time its
    index is found in `planets_closest`.
    
    Returns the modified `planets_scores` list. 
    """

    # for "element" in closest
        # scores[element] = scores + 1
    
    # return planets_scores
    ...

def planets_decays(planets_scores):
    """
    Multiplies every element in `planets_scores` by 0.9.

    Returns the modified `planets_scores`.
    """

    # for i in list
        # list[i] = list[i] * 0.9 # Potentially softcodable

    # return list or whatever
    ...

def add_to_dataset(planet_dataset, planets_scores, time):
    """
    Copies `planets_scores`, inserts `time` at the first index of
    the copy, then appends the modified copy to `planet_dataset`.
    
    Returns the modified `planet_dataset`.

    The copy, added to `planet_dataset`, looks like this:
    `[time, planets_scores[0], planets_scores[1], ..., planets_scores[7]]`
    """

    # copy list
    # use insert for time (on the copy)
    # append copy to dataset

    # return new dataset
    ...

def simulate(length):
    """
    Runs a simulation of `length` days long and adds the collected data to a dataset.

    When going through each iteration, it moves the planets, then scores the planets.

    Returns the resultant dataset that represents the scores appearing throughout the
    simulation.
    """

    # distant for loop, add an indent to the following
    # for loop length / simulation length softcodable
    
    # add to time
    # move planets, calculate and set position with `planets_positions`
    # analyze planets, calculate and set closests analysis with `planets_closests`
    # add to scores after getting resutls from `planets_adds`
    # ditto, but with `planets_decays`
    # call `add_to_dataset`

    # return dataset
    ...

def write_dataset(dataset, path):
    """
    Stores `dataset` as a .csv file in `path`.
    """

    # initialize a string

    # for each row in the dataset:
        # append `element,element,element` + `\n`
    # remove the last \n

    # with _ as _ (write) # path potentially softcodable
        # write a string to the file
    ...

def main():
    """
    Writes a dataset representing a simulation that it runs over
    the course of multiple simulated days.
    """

    # Simulate the data, stored as `planet_dataset`, by invoking
    # `simulate()`.

    # Write the data, initially stored as `planet_dataset`, to
    # "scores.csv", by invoking `write_dataset()`.
    ...

if (__name__ == "__main__"):
    main()