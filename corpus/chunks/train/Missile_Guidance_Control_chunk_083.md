<table><tr><td></td><td>Roll Body Axis ( $X_b$ )</td><td>Pitch Body Axis ( $Y_b$ )</td><td>Yaw Body Axis ( $Z_b$ )</td></tr><tr><td>Angular Rates</td><td>P</td><td>Q</td><td>R</td></tr><tr><td>Velocity Components</td><td>u</td><td>v</td><td>w</td></tr><tr><td>Aerodynamic Force Components</td><td> $F_X$ </td><td> $F_Y$ </td><td> $F_Z$ </td></tr><tr><td>Aerodynamic Force Coefficients</td><td> $C_D$ </td><td> $C_Y$ </td><td> $C_L$ </td></tr><tr><td>Aerodynamic Moment Coefficients</td><td> $C_l$ </td><td> $C_m$ </td><td> $C_n$ </td></tr></table>

The basic aerodynamic forces are commonly defined in terms of dimensionless coefficients, the flight dynamic pressure, and a reference area. For missiles that skid (yaw) to turn (see Section 3.3.2 for more details), the basic aerodynamic forces are illustrated in Figure 3.2 and are calculated as follows [2], [6]:

$$\text { Drag: } \quad D = C _ {D} q S, \tag {3.1}\text { Lift: } \quad L = C _ {L} q S, \tag {3.2}\text { Side Force: } \quad F _ {Y} = C _ {Y} q S, \tag {3.3}$$

where

$$C _ {D} = \text { Coefficient of drag in the wind axis system },C _ {L} = \text { Coefficient of lift in the wind axis system },C _ {Y} = \text { Side force coefficient },q = \text { Free - stream dynamic pressure at a point far from the airfoil } = \frac {1}{2} \rho V ^ {2},S = \text { Reference area, usually the area of one of the airfoils },V = \text { Free - stream velocity },\rho = \text { Atmospheric density } = 2. 3 7 6 9 \times 1 0 ^ {- 3} \mathrm{lb-sec} ^ {2} - \mathrm{ft} ^ {- 4}\text { at sea level (see also Appendix D). }$$

For missiles that roll to turn, drag is the same as in (3.1), but the lift and side force are as follows:

$$\operatorname{Lift} = C _ {L T} (\cos \phi) q S, \tag {3.4}\text { Side Force } = C _ {L T} (\sin \phi) q S, \tag {3.5}$$

where

$$C _ {L T} = \text { Total lift coefficient in the maneuver plane } = (C _ {L} ^ {2} + C _ {Y} ^ {2}) ^ {1 / 2},\phi = \text { Roll angle }.$$

For the purposes of the discussion in this book, the three most important aerodynamic force coefficients are commonly defined as∗

$$C _ {L} = L / q S,C _ {D} = D / q S,C _ {M} = M / q S d,$$

where M is the moment and d is the mean missile diameter from a body cross-section. Figure 3.3 illustrates the aerodynamic forces relative to the wind-axis system.

The aerodynamic forces may also be expressed in the form
