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

- Make an upper-level outline as to how the functions are laid out

- Top-down outline of the functions

- Implement each of the functions

simulate()

- update docstring

write_dataset()

- needs header

""" # Tasks

# Dynamic similation variables
planets_x = []
planets_y = []
planets_closest = []
planets_scores = []

# Dataset
planet_dataset = []
"""A non-jagged 2D list. Each row stores the time of the simulation, then the scores of each planet."""

def move_planets(time):
    """
    Calculates the position of the planets using the updated `time`,
    then sets their new positions in the `planets_x` and `planets_y`
    tables.
    """
    ...

def analyze_planets():
    """
    Updates `planets_closest` to reflect the closest destination to
    each planet.
    """
    ...

def score_planets():
    """
    Adds +1 to each planet's score if it was listed as a closest
    destination in `planets_closest`.
    """
    ...

def decay_planets():
    """
    Multiplies every planet's score by 0.9.
    """

def add_to_dataset():
    ...

def simulate():
    """
    Runs a simulation using the following rules:

    [RULES TBD]
    """

    # distant for loop, add an indent to the following
    
    # add to time
    # call `move_planets`
    # call `analyze_planets`
    # call `score_planets`
    # call `decay_planets`
    # call `add_to_dataset`
    ...

def write_dataset(dataset):
    """
    Stores `dataset` as a .csv file.
    """

    # initialize a string

    # for each row in the dataset:
        # append `element,element,element` + `\n`
    # remove the last \n

    # with _ as _ (write)
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