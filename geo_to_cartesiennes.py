from math import *
from dms_to_degrees import *
from Ellepsoide_parametres import*


def Geo2Cartesian(phi, lam, h, a, inv_f):

    lam = radians(lam)
    phi = radians(phi)
    e_squared, e_prime_squared = ellipsoid_parameters(a, inv_f)
    w = sqrt(1-(e_squared*pow(sin(phi), 2)))
    n = a/w
    x = (n+h)*cos(lam)*cos(phi)
    y = (n+h)*sin(lam)*cos(phi)
    z = (n*(1-e_squared)+h)*sin(phi)
    return x, y, z
