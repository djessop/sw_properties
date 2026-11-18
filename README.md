# sw_properties
Provides physical properties (density, viscosity, conductivity, ...) of sea/salt water.  Based on matlab files from http://web.mit.edu/seawater/

## Usage:
```python
from sw_properties import rho_sw, kinematic_viscosity, dynamic_viscosity

S = 20.5  # water salinity/[g/kg]
T = 20.   # water temperature/[°C]

rho = rho_sw(T, S)
print(f"Density of water at {T:.1f} °C with salinity {S:.2f} g/kg: {rho:.3f} g/cm³")
print(f"Kinematic viscosity of water at {T:.1f} °C with salinity {S:.2f} g/kg: {kinematic_viscosity(T, S):.3f} cm²/s")
```

By default, temperatures are given in degrees Celsius (°C), and salinity in units of g/kg (or ppt).  However, other units can be specified by using the `uT` and `uS` keywords


|uT | definition |uS | definition |
|---|------------|---|------------|
|'C'| degrees Celsius | 'ppt' | parts per thousand, or g/kg |
|'K'| Kelvin | 'ppm' | parts per million, or mg/kg |
|'R'| Rankine | 'w'  | weight ratio, or kg/kg |
|'F'| Farenheit | '% | percent, or 100 * g /kg |

```python
S /= 1e3    # kg/kg
T += 273.15 # K
print(f"Kinematic viscosity of water at {T:.1f} K with salinity {S:.3f} kg/kg: {kinematic_viscosity(T, S, uT='K', uS='w'):.3f} cm²/s")
```

## Provides:
```
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