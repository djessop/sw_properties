#!/usr/bin/python

"""
    SW_Kviscosity
"""

from sw_properties.sw_utils import parse_units
from sw_properties.sw_density import rho_sw
from sw_properties.sw_viscosity import dynamic_viscosity


def kinematic_viscosity(T, S=0.0, uT='C', uS='ppt', output_units='cgs'):
    """
    Returns an estimate for the kinematic viscosity of salt water.

    See also
    --------
    dynamic_viscosity, rho_sw
    """
    T, S = parse_units(T, S, uT, uS)
    return dynamic_viscosity(T, S) / rho_sw(T, S)
