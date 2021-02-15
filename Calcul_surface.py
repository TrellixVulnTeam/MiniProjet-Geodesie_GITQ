from math import *


def calculate_area(lam1, lam2, phi1, phi2, a, inv_f):
    phi1 = phi1 * pi / 180
    phi2 = phi2 * pi / 180
    lam1 = lam1 * pi / 180
    lam2 = lam2 * pi / 180
    f = 1/inv_f
    e = sqrt(1 - pow((1 - f), 2))
    b = a * (1 - f)
    phi2_f = (0.5 / e) * log((1 + e * sin(phi2)) / (1 - e * sin(phi2))) + sin(phi2) / (1 - pow(e, 2) * pow(sin(phi2), 2))

    phi1_f = (0.5 / e) * log((1 + e * sin(phi1)) / (1 - e * sin(phi1))) + sin(phi1) / (1 - pow(e, 2) * pow(sin(phi1), 2))

    s = 0.5 * pow(b, 2) * (lam2 - lam1) * (phi2_f - phi1_f)
    round(s, 6)

    return s

