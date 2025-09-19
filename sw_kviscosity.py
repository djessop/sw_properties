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

    Parameters
    ----------
    T : float or array-like
        Temperature
    S : float or array-like
        Salinity 
    uT : str
        Units of temperature, default is 'C' for degC
    uS : str
        Units of salinity, default is 'ppt' (equiv. to g/kg)
    output_units : str
        Units system for the output either 'cgs' or 'mks', default is 'cgs'

    Note that the subfunctions use the fractional salinity, whereas the input 
    salinity is in ppt by default.  This is dealt with using the "parse_units"
    routine from sw_utils.  
    
    See also
    --------
    dynamic_viscosity, rho_sw
    """
    T, S = parse_units(T, S, uT, uS)
    return dynamic_viscosity(T, S) / rho_sw(T, S)
