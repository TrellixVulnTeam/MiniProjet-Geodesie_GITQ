from math import *
from sympy import *


def prob_direct(phi1, lam1, a12, s, r):
    sigma = s / r
    phi1 = radians(phi1)
    a12 = radians(a12)
    phi2 = degrees(asin(sin(phi1) * cos(sigma) + cos(phi1) * sin(sigma) * cos(a12)))
    lam2 = lam1 + degrees(acot((1/sin(a12))*((cot(sigma) * sin((pi/2) - phi1)) - (cos((pi/2) - phi1) * cos(a12)))))
    a21 = degrees(acot((1 / sin(a12)) * (cos(sigma)*cos(a12) - tan(phi1) * sin(sigma))))

    return phi2, lam2, a21


def prob_indirect(phi1, phi2, lam1, lam2, r):

    lam1 = radians(lam1)
    lam2 = radians(lam2)
    phi1 = radians(phi1)
    phi2 = radians(phi2)
    d_lam = fabs(lam2 - lam1)
    s = acos((sin(phi1) * sin(phi2)) + (cos(phi1) * cos(phi2) * cos(d_lam)))
    s = s * r
    a12 = acot(((tan(phi2) * cos(phi1))/sin(d_lam)) - (sin(phi1) * cot(d_lam)))
    a12 = degrees(a12)
    a21 = acot(-(((tan(phi1) * cos(phi2))/sin(d_lam)) - (sin(phi2) * cot(d_lam))))
    a21 = degrees(a21)

    return s, a12, a21


