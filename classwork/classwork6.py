"""
    Name: James Michael Crespo
    Email: james.crespo64@myhunter.cuny.edu
    Resources: the internet
    I attended lecture today.
    Row: 9
    Seat: 93
"""

import numpy as np
import scipy.stats


def compute_smoothing(xes, points):
    """this function functions"""
    result = np.zeros(len(xes))
    for p_val in points:
        result += scipy.stats.norm.pdf(xes, loc=p_val, scale=0.5)
    return result
