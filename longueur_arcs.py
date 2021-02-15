from math import *


def long_arc_meridian(phi1, phi2, a, inv_f):
    phi1 = phi1 * pi / 180
    phi2 = phi2 * pi / 180
    f = 1 / inv_f
    e = sqrt(1 - pow((1 - f), 2))

    A = 1 + (3 / 4) * pow(e, 2) + (45 / 64) * pow(e, 4) + (175 / 256) * pow(e, 6) + (11025 / 16348) * \
        pow(e, 8) + (43659/65536) * pow(e, 10)
    B = (3 / 4) * pow(e, 2) + (15 / 16) * pow(e, 4)+(525 / 512) * pow(e, 6) + (2205 / 2048) *\
        pow(e, 8) + (72765 / 65536)*pow(e, 10)
    C = (15 / 16) * pow(e, 4) + (105 / 256) * pow(e, 6) + (2205 / 4096) * pow(e, 8) + (10395 / 16348) * pow(e, 10)
    D = (35 / 512) * pow(e, 6) + (315 / 2048) * pow(e, 8) + (31185 / 131072) * pow(e, 10)
    E = (315 / 16384) * pow(e, 8) + (3465 / 65536) * pow(e, 10)
    F = (639 / 131072) * pow(e, 10)

    alpha = A * a * (1 - pow(e, 2))
    beta = (B / 2) * a * (1 - pow(e, 2))
    gamma = (C / 4) * a * (1 - pow(e, 2))
    delta = (D / 6) * a * (1 - pow(e, 2))
    eps = (E / 8) * a * (1 - pow(e, 2))
    mu = (F / 10) * a * (1 - pow(e, 2))

    s1 = alpha * phi1 - beta * sin(2 * phi1) + gamma * sin(4 * phi1) - delta * sin(6 * phi1) + eps * sin(8 * phi1) - \
        mu*sin(10 * phi1)
    s2 = alpha * phi2 - beta * sin(2 * phi2) + gamma * sin(4 * phi2) - delta * sin(6 * phi2) + eps * sin(8 * phi2) - \
         mu * sin(10 * phi2)
    s = s2-s1

    return s


def long_arc_parallele(phi, lam1, lam2, a, inv_f):
    f = 1 / inv_f
    phi = phi * pi / 180
    e = sqrt(1 - pow((1 - f), 2))
    DL = abs((lam2 - lam1)) * pi / 180
    w = sqrt(1 - pow(e, 2) * pow(sin(phi), 2))
    N = a / w
    R = N * cos(phi)
    L = R * DL
    return L





