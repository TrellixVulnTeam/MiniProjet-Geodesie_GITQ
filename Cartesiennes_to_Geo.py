from math import *
from Ellepsoide_parametres import *




def cartesian2geo(x, y, z, a, inv_f, epsilon):
    f = 1 / inv_f
    b = a * (1 - f)
    e_squared, e_prime_squared = ellipsoid_parameters(a, inv_f)
    if x != 0:
        lam = atan(y / x)

    else:
        print('lambda cant be calculated because the denominator is null!')
    phi_0 = atan(z/sqrt(pow(x, 2)+pow(y, 2)))
    #e_squared, e_prime_squared = ellipsoid_parameters()
    n_0 = a/sqrt(1-(e_squared*pow(sin(phi_0), 2)))
    h_0 = (sqrt(pow(x, 2)+pow(y, 2))/cos(phi_0))-n_0
    phi_1 = atan((z / sqrt(pow(x, 2) + pow(y, 2))) * (1 / (1 - (e_squared * (n_0 / (n_0 + h_0))))))
    n_1 = a / (sqrt(1 - (e_squared * pow(sin(phi_1), 2))))
    h_1 = (sqrt(pow(x, 2) + pow(y, 2)) / cos(phi_1)) - n_1
    phi_n = phi_1
    phi_n_1 = phi_0
    n_n_1 = n_1
    h_n_1 = h_1
    while fabs((phi_n-phi_n_1)/phi_n) > epsilon:
        phi_n_1 = phi_n

        phi_n = atan((z/sqrt(pow(x, 2)+pow(y, 2)))*(1/(1-(e_squared*(n_n_1/(n_n_1+h_n_1))))))
        n_n = a/(sqrt(1-(e_squared*pow(sin(phi_n), 2))))
        h_n = (sqrt(pow(x, 2)+pow(y, 2))/cos(phi_n))-n_n
        n_n_1 = n_n
        h_n_1 = h_n
    lam = degrees(lam)
    phi = degrees(phi_n_1)
    return phi, lam, h_n_1






