def parse_units(T=20., S=0., uT='C', uS='ppt'):
    '''
    Returns temperature and salinity in degC and ppt, the default values for
    this suite of programmes.

    Also checks that the variables are within the tolerated range.
    '''
    import numpy as np

    # Check types, and parse as necessary
    if isinstance(S, int):
        S = float(S)
    if isinstance(S, np.ndarray):
        S = S.astype(float)

    # Temperature unit checks
    uT = uT.lower()
    if uT == 'c':
        pass
    elif uT == 'k':
        T -= 273.15
    elif uT == 'f':
        T = 5./9. * (T - 32.)
    elif uT == 'r':
        T = 5./9. * (T - 491.67)
    else:
        raise TypeError('Not a recognized temperature unit.  '
                        + 'Please use "C", "K", "F", or "R"')
    uT = 'C'
    
    # Salinity unit checks
    uS = uS.lower()
    if uS == 'ppt':
        pass
    elif uS == 'ppm':
        S = S / 1000
    elif uS == 'w':
        S = S * 1000
    elif uS == '%':
        S = S * 100
    else:
        raise TypeError('Not a recognized temperature unit.  '
                        + 'Please use "ppt", "ppm", "w", or "%"')
    uS = 'ppt'

    # Warnings for temperature or salinity out of range
    assert (np.logical_and(0 <= T, T <= 180).any() \
            and np.logical_and(0 <= S, S <= 160).any()), \
        'Temperature and/or salinity are outside of accepted ranges: ' \
        '0 <= T <= 180 degC, 0 <= S <= 160 g/kg'
        
    S /= 1000   # Following routines require S in [kg/kg]

    return T, S


