# ICAO Standard Atmosphere Input/Output:

The input to the atmosphere model is

z = altitude of interest [m].

The output from the model is

$T _ { a }$ = ambient atmospheric temperature at altitude $z \left[ K \right]$ ,

$P _ { a }$ = ambient atmospheric pressure at altitude $z \ [ N / m ^ { 2 } ]$ ,

$\rho _ { a }$ = ambient atmospheric density at altitude $z \ [ k g / m ^ { 3 } ]$ ,

Va = speed of sound at altitude z [m/sec].

While not a factor in some studies, altitude can be an important consideration. As altitude increases, density decreases, leading to a lower dynamic pressure for a given speed. This leads to lower drag, so that missile deceleration is less pronounced, but it also leads to lower moments and forces, so the missile loses some maneuverability. Also, since the speed of sound is a function of altitude, the missile Mach number for a given speed depends on altitude. Missile aerodynamic properties (e.g., drag coefficient, lift coefficient, and moment coefficient) depend on Mach number and so will change with altitude, giving different missile aerodynamic responses.

Pressure, temperature, air density, and speed of sound are calculated using pressure curve fits and temperature gradients derived from the 1962 standard atmosphere data. The input altitude and the calculated atmospheric conditions are all in metric units. Four data tables of the 1962 U.S. standard atmosphere data are used to calculate the atmosphere parameters: temperature, temperature gradient, pressure, and corresponding reference altitudes. Table D.1 shows these four data tables combined [1]. These tables are referenced using altitudes expressed in geopotential meters. One geopotential meter is defined as the vertical distance through which a one-kilogram mass must be moved to increase its potential energy by 9.80665 joules [2]. Thus, a given input altitude h in geometric meters is converted to altitude H in geopotential meters using the expression [2]

$$H = [ R _ {E} / (R _ {E} + h) ] h, \tag {D.9}$$

where

H = geopotential altitude,

h = geometric altitude,

R = radius of the Earth = 6, 356, 766 m corresponding to $4 5 ^ { \circ }$ latitude on a nonperfect spherical Earth model.

Table D.1. 1962 U.S. Standard Atmosphere Data Tables
