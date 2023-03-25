"""
    Name: James Michael Crespo
    Email: james.crespo64@myhunter.cuny.edu
    Resources: the internet
    I attended lecture today.
    Row: 8
    Seat: 92
"""
import numpy as np


def approxDigits(numComponents, coefficients, mean, components):
    """
    This function has four inputs and returns an array containing the approximation:
    :param numComponents: the number of components used in approximation. Expecting (0 to 64).
    :param coefficients: an array of coefficients, outputted from PCA().
    :param mean: an array representing the mean of the dataset.
    :param components: an array of the components computed by PCA() analysis.
    The function returns the approximation image (flattened array) of the mean
    and sum of the first numComponents terms
    (i.e. coefficients[i] * components[i])
    """
    total_sum = np.zeros(shape=len(coefficients))
    for index in range(0, numComponents):
        temp_sum = coefficients[index] * components[index]
        total_sum += temp_sum
    return mean + total_sum
