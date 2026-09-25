# starliner-strife
Analyzing a network of interconnected planetary colonies.

Run `python planets.py` to run the simulation.

# How the Simulation Works
Given a 2D model of the solar system's eight planets and their
orbits, the planets will be scored over time as they move about their
orbits. If a planet is a closest destination to more planets, the
planet will have a higher score. The planets' distances will vary
over time, so the scores will thus vary.

The scores are calculated with the following process, run through
each step of the simulation. First, the posiitons of the planets
are calculated. Then, the closest destination to each respective
planet is determined. For each cloest destination listed, the
planet listed as a closest destination will have its score added
by +1 for each step of the simulation. Then, regardless of if the
planet was listed as a closest destination, all eight planets'
scores will be multiplied by 0.9 to serve as a decay factor when
planets aren't the closest destinations for a long time.

A `.csv` file will contain the planet's scores over time. Each row
will contain the scores of the planets at the end of each step.
The first column will contain the time elapsed, in days, and the
rest of the columns will contain the scores of the planets in
ascending order by semi-major axis.