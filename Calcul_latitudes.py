from math import *
from dms_to_degrees import*
from Ellepsoide_parametres import*
from Cartesiennes_to_Geo import *


def calculate_latitudes(a, inv_f, z, phi):

    f = 1 / inv_f
    b = a * (1 - f)
    phi = radians(phi)
    beta = asin(z/b)
    e_squared, e_prime_squared = ellipsoid_parameters(a, inv_f)
    x = e_squared * pow(sin(phi), 2)
    w = sqrt(1 - x)
    o_p = (a/w)*sqrt(1+((e_squared-2)*e_squared*pow(sin(phi), 2)))
    psi = asin(z/o_p)
    beta = degrees(beta)
    psi = degrees(psi)
    return beta, psi


def calculate_psi_beta(a, inv_f, phi):
    f = 1 / inv_f
    b = a * (1 - f)
    phi = radians(phi)
    beta = atan((b/a)*tan(phi))
    psi = atan((pow(b, 2)/pow(a, 2))*tan(phi))
    beta = degrees(beta)
    psi = degrees(psi)
    return beta, psi


def calculate_beta_phi(a, inv_f, psi):
    f = 1 / inv_f
    b = a * (1 - f)
    psi = radians(psi)
    beta = atan((a/b)*tan(psi))
    phi = atan((pow(a, 2)/pow(b, 2))*tan(psi))
    beta = degrees(beta)
    phi = degrees(phi)
    return phi, beta


def calculate_phi_psi(a, inv_f, beta):
    f = 1 / inv_f
    b = a * (1 - f)
    beta = radians(beta)
    phi = atan((a/b)*tan(beta))
    psi = atan((b/a)*tan(beta))
    phi = degrees(phi)
    psi = degrees(psi)
    return phi, psi


