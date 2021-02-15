from math import *
from dms_to_degrees import *
from dms_to_degrees import*
from Ellepsoide_parametres import*


def curvature_radius(a, inv_f, phi, alpha):
    e_squared, e_prime_squared = ellipsoid_parameters(a, inv_f)
    alpha = (alpha*pi)/180
    phi = (phi*pi)/180
    x = e_squared*pow(sin(phi), 2)
    w = sqrt(1-x)
    # m:rayon de courbure du méridien
    m = (a*(1-e_squared))/pow(w, 3)
    # n:rayon de courbure du premier vertical
    n = a/w
    # r_alpha:rayon de courbure d'une section normale d'azimut alpha
    r_alpha = ((m*pow(sin(alpha), 2))+(n*pow(cos(alpha), 2)))/(m*n)

    return m, n, r_alpha


def rayon_alpha(rm, n, alpha):
    alpha = (alpha*(pi/2))/90
    r_alpha = rm * (pow(sin(alpha), 2) + n * pow(cos(alpha), 2)) / rm * n
    return r_alpha
