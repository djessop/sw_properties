#!/usr/bin/python

"""
    SW_Kviscosity
"""

from SW_Properties.SW_Utils import parse_units
from SW_Properties.SW_Density import rho_sw
from SW_Properties.SW_Viscosity import dynamic_viscosity


def kinematic_viscosity(T, S=0.0, uT='C', uS='ppt', output_units='cgs'):
    T, S = parse_units(T, S, uT, uS)
    return dynamic_viscosity(T, S) / rho_sw(T, S)
