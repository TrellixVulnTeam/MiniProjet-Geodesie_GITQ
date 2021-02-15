from math import *


def ellipsoid_parameters(a, inv_f):

    f = 1/inv_f
    b = a*(1-f)

    e_squared = (pow(a, 2)-pow(b, 2))/pow(a, 2)
    e_prime_squared = (pow(a, 2)-pow(b, 2))/pow(b, 2)
    return e_squared, e_prime_squared


def ellipsoid_parameters_all(a, inv_f):
    f = 1 / inv_f
    b = a * (1 - f)
    alpha = acos(b / a)
    c = pow(a, 2) / b

    e_squared = (pow(a, 2) - pow(b, 2)) / pow(a, 2)
    e_prime_squared = (pow(a, 2) - pow(b, 2)) / pow(b, 2)
    return e_squared, e_prime_squared, alpha, c, b


