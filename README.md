# sw_properties
Provides physical properties (density, viscosity, conductivity, ...) of sea/salt water.  Based on matlab files from http://web.mit.edu/seawater/

## Provides:
```bash
.
├── sw_density.py
|   ├── rho_plain_water: density of plain water as a function of temperature
|   ├── delta_rho: density increase due to salinity
|   ├── rho_plain: a wrapper for rho_plain_water
|   ├── rho_sw: density of water as a function of both temp. and salinity
|   ├── drho_plain_water_dT: derivative of rho_plain_water wrt temperature
|   ├── drho_plain_water_ds: derivative of rho_plain_water wrt salinity
|   ├── ddelta_rho_dT: derivative of delta_rho wrt temperature
|   ├── ddelta_rho_ds: derivative of delta_rho wrt salinity
|   ├── drho_sw_dT: derivative of rho_sw wrt temperature
|   └── drho_sw_ds: derivative of rho_sw wrt salinity
|
├── sw_kviscosity.py
|   └── kinematic_viscosity: kinematic viscosity of salt water
|
├── sw_viscosity.py
|   └── dynamic_viscosity: dynamic viscosity of salt water
|
└── sw_utils.py
    └── parse_units: utility for providing compatible units 
```

## Usage:
```python
from sw_properties import rho_sw, kinematic_viscosity, dynamic_viscosity
```