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

Other

- Add parameters to functions to allow for testability

- Add ".csv" to gitignore

- Split distance() to complete parameterization

- Write tests for simulate()

- Update descriptions of return descriptions in docstring

""" # Tasks

# Static configuarion variables
PLANETS_PERIODS = []
PLANETS_SEMIS = []

# Dynamic similation variables
planets_x = []
planets_y = []
planets_closest = []
planets_scores = []

# Dataset
planet_dataset = []
"""A non-jagged 2D list. Each row stores the time of the simulation, then the scores of each planet."""

def move_planets(planets_periods, planets_semis, time):
    """
    Calculates the position of the planets using the updated `time`,
    then sets their new positions in the `planets_x` and `planets_y`
    tables.

    Returns the list-of-x-coords and list-of-y-coords.
    """
    # for loop (0 - 7)
        # theta = time / period
        # x = cos(th)
        # y = sin(th)
        # update planets_x
        # update planets_y
    ...

def distance_expression(x1, y1, x2, y2):
    """
    Gets the distance between the two points (`x1`, `y1`) and (`x2`, `y2`).
    """

    # Pythagorean expression
    ...

def distance_planets(planets_x, planets_y, i, j):
    """
    Calculates the distance between planet `i` and planet `j`.

    Also takes in the lists of the x and y coordinates of the planets
    (`planets_x` and `planets_y`)
    """

    # Get positions of `i` and `j`, stored as four cartesian corrdinate comps
    # Pythagorean expression `distance_expression()`
    ...

def closest_planet(planets_x, planets_y, i):
    """
    Returns the index of the closest destination to planet `i`.

    Also takes in the lists of the x and y coordinates of the planets
    (`planets_x` and `planets_y`)
    """

    # Variable distance_is_set
    # Variable min_distance
    # Variable held_index_j

    # For j = 0, 7
        # Get distance from i to j using `distance_planets()`
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

def analyze_planets(planets_x, planets_y):
    """
    Updates `planets_closest` to reflect the closest destination to
    each planet.

    Done by analyzing the coordinates of planets with the given lists
    of x and y coordinates respectively.

    Returns a list of closest planets.
    """

    # for i = 0, 7
        # get the closest planet j using `closest_planet()`
        # place j in index i of planets_closest

    # return planets_closest
    ...

def score_planets(planets_scores, planets_closest):
    """
    Adds +1 to an element in `planets_scores` each time its
    index is found in `planets_closest`.
    """

    # for "element" in closest
        # scores[element] = scores + 1
    
    # return planets_scores
    ...

def decay_planets(planets_scores):
    """
    Multiplies every element in `planets_scores` by 0.9.
    """

    # for i in list
        # list[i] = list[i] * 0.9 # Potentially softcodable

    # return list or whatever
    ...

def add_to_dataset(planet_dataset, planets_scores, time):
    """
    Copies `planets_scores`, inserts `time` at the first index of
    the copy, then appends the modified copy to `planet_dataset`.

    The copy looks like this:
    `[time, planets_scores[0], planets_scores[1], ..., planets_scores[7]]`
    """

    # copy list
    # use insert for time (on the copy)
    # append copy to dataset

    # return new dataset
    ...

def simulate():
    """
    Runs a simulation and adds the collected data to a dataset.

    When going through each iteration, it moves the planets, then scores the planets.
    """

    # distant for loop, add an indent to the following
    # for loop length / simulation length softcodable
    
    # add to time
    # call `move_planets`
    # call `analyze_planets`
    # call `score_planets`
    # call `decay_planets`
    # call `add_to_dataset`
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